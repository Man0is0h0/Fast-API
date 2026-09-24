
from app import oauth2

from .. import models,schemas
from ..database import get_db
from fastapi import Depends,HTTPException,Response,APIRouter
from sqlalchemy.orm import Session
from typing import List

router=APIRouter(
    prefix="/posts",
    tags=['Posts']
)






##All Posts
@router.get("/",response_model=List[schemas.Post]) 
def get_all_posts(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
                    # cursor.execute("""SELECT * FROM posts ORDER BY id ASC""")
                    # posts=cursor.fetchall()
    if not posts:
        raise HTTPException(status_code=404,detail="No Posts Available")
    return posts



##Post by id
@router.get("/{id}",response_model=schemas.Post)
def get_post_by_id(id:int,db:Session=Depends(get_db)):
                                # cursor.execute("""SELECT * FROM posts WHERE ID= %s""",(str(id)))
                                # post=cursor.fetchone()
    # post=find_post(id)
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if post is None:
        raise HTTPException(status_code=404,detail=f"The post with post id: {id} does not exist!!!")
    return post
                                                    # response.status_code = 404
                                                    # return {
                                                    #     "error": "The post that you are looking for does not exist!!!"
                                                    # }
#POST



# @app.get("/sqlalchemy")
# def test_posts(db:Session=Depends(get_db)):
#     posts=db.query(models.Post).all()
#     return {"Data": posts}





##Create a post
@router.post("/",status_code=201,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db:Session=Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
    new_post=models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
                        # cursor.execute("""INSERT INTO posts(title,content,published) VALUES(%s, %s, %s) RETURNING *""",(post.title,post.content,post.published))
                        # new_post=cursor.fetchone()
                        # conn.commit()
                        # return {"data":new_post} 
                                                    # post_dict=post.model_dump()
                                                    # post_dict['id']=randrange(0,1000000000)
                                                    # my_posts.append(post_dict)




#DELETE
##Delete a post

@router.delete("/{id}",status_code=204)
def delete_post(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)
                        # cursor.execute("""DELETE FROM posts WHERE ID= %s RETURNING*""",(id,))
                        # conn.commit()
                        # post=cursor.fetchone()

    # index=find_index_post(id)
    if post.first() is None:
        raise HTTPException(status_code=404,detail=f"The post with post id: {id} does not exist!!!")
    # my_posts.pop(index)
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=204)




#UPDATE
#PUT
@router.put("/{id}",response_model=schemas.Post)
def update_entire_post(id:int, post:schemas.PostCreate,db:Session=Depends(get_db)):
                                                    # print(post)
                                                    # ind=find_index_post(id)
                            # cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE ID=%s RETURNING *""",(post.title,post.content,post.published, id))
                            # conn.commit()
                            # updated_post=cursor.fetchone()
    updated_post=db.query(models.Post).filter(models.Post.id==id)
    if updated_post.first() is None:
            raise HTTPException(status_code=404,detail=f"The post with post id: {id} does not exist!!!")
    updated_post.update(post.model_dump(),synchronize_session=False)
    db.commit() 
    return updated_post.first()
                                                    # post_dict=post.model_dump()
                                                    # post_dict["id"] = id
                                                    # my_posts[ind]=post_dict
 