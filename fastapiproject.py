from fastapi import FastAPI

app=FastAPI() # app is variable for FastApi instance creating here
@app.get('/') #@ indicates the decorator route for root url of webapp
def index():
    return {'data':{'pavan':'mudunuri'}} #return the data in json format output


@app.get('/about') #about indiactes the about the page
def about():
    return{'about':{'about the page'}}

@app.get('/')  #fetch with blog id=id ip add last /id
def idx():
    return{'data':'blog list'}


# fetch comments of the blog id =id ip add last/blog
@app.get('/blog/{id}')
def show(id):
    return {'data':1}



# fetch comments of the blog id =id ipadd last/comments
@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1' ,'2'}}
# defaultly we get data in string 
# if we want data in int we have to mention id:int like this.
#definng the intiger
@app.get('/blog/{id}')
def shed(id: int):
    return {'data': id}



@app.get('/blog/{id}')
def shed(id: str):
    return {'data': id}


@app.get('/blog/unpublished')
def unpublished():
    return{'data': 'all unpublished blogs'}