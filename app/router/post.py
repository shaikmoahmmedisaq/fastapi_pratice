from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas,utills ,oauth2
from .. database import get_db
from typing import Optional ,List 
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",tags=['posts']
)

@router.get("/",response_model=List[schemas.PostOUT])
# @router.get("/")
def get_post(db: Session = Depends(get_db),current_id:int= Depends(oauth2.get_current_user),
             limits:int =10,skip:int = 0,search: Optional[str] =""):
    # cursor.execute("""select * from posts """)
    # post=cursor.fetchall()lim
    # print(search)
    # print(current_id.id)
    # posts=db.query(models.Post).filter(models.Post.owner_id == current_id.id).all()
    # posts=db.query(models.Post).filter(models.Post.title.contains(search)
    #                                    ).limit(limits).offset(skip).all()
    
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)
                                       ).limit(limits).offset(skip).all()
    # print(result)
    
    # print(posts)
    return post

@router.post('/',response_model=schemas.Post)
def create_post(post:schemas.PostCreate,db: Session = Depends(get_db),current_id:int= Depends(oauth2.get_current_user)):#get_current_user=int= Depends(oauth2.get_current_user)
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,
    #                (post.title,post.content,post.published))
    # new_post= cursor.fetchone()
    # conn.commit()
    # print(**post.dict())
    # print(current_id.id)
    new_post=models.Post(owner_id = current_id.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}",response_model=schemas.PostOUT) 
def get_post(id:int,response:Response,db :Session = Depends(get_db),current_id:int= Depends(oauth2.get_current_user)):
    # print(type(id))
    # cursor.execute("""SELECT * from  posts WHERE  id = %s""",(str(id)))
    # post = cursor.fetchone()
    # print( post)
    # print(current_id.id)
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post =  db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True
        ).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'post id not  found {id }')
    # if post.owner_id != current_id.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail="Not authorized to perform requested action")
    return post

@router.delete('/{id}',response_model=schemas.Post) 
def delete_post(id:int,db :Session = Depends(get_db),current_id:int= Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts where id = %s returning *""",(str(id)))
    # delete_post = cursor.fetchone()
    # print(delete_post)
    # conn.commit()
    # post_query =db.query(models.Post).filter(models.Post.id == id)
    # post = post_query.first()
    # if post == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not exists")
    # # print(index)
    # # mypost.pop(index) 
    # if post.owner_id != current_id.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not auth")
    # post_query.delete(synchronize_session=False)
    # db.commit()
    # return Response(status_code=status.HTTP_204_NO_CONTENT)
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != current_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}',response_model=schemas.Post) 
def update_post(id:int,updated_post:schemas.PostCreate,db :Session = Depends(get_db),current_id:int= Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title = %s ,content = %s ,published=%s where id = %s RETURNING * """,
    #                (post.title,post.content,post.published,str(id)))
    # # print(post)
    # # index = find_index_post(id) 
    # update_post = cursor.fetchone()
    # print(update_post)
    # conn.commit()
    post_query =db.query(models.Post).filter(models.Post.id == id)
    post =post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not exists")
    if post.owner_id != current_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not auth")
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()

