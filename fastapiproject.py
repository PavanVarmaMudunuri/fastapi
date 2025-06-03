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
#queary parameters
'''Query parameters are used to pass optional or required values in the URL after ?'''

@app.get('/blog')
def idx(limit=10, published: bool = True, sort: Optional[str]=None):
    #here 10 blogs can be published
    if published:

        return{'data': f'{limit}published blogs from the db'}
    else:
        return{'data':f'{limit} blogs from the db'}
    

@app.get('/blog/{id}/coment')
def comment(id, limit=10):
    #fetch the comments of blog with id= id
    return{'data':{'1', '2'}}



#Requst Body
'''A request body contains data sent from the client to the API, typically in JSON format
Uses Pydantic models for structured data validation.
Request body is automatically parsed and validated.

Features

Automatic Type Conversion → Converts request body fields into specified types.
Validation & Error Handling → Ensures correct data types and required values.
Interactive API Docs → /docs generates Swagger UI for testing requests.
Combining with Path & Query Parameters → Supports mixed requests.
Editor Support → Provides autocompletion and error detection.
Built-in Schema Generation → FastAPI auto-generates OpenAPI schemas.'''

class Blog(BaseModel):
    title: str
    body:str
    published:Optional[bool]
    
@app.post('/blog')
def create_blog(request: Blog):
    return{'data': "blog is craeted"}

