from django.http import HttpResponse


def home(request):
    html = '''
  <br/>
  <center>
     <h1 style='background-color=red'>Reza Rezaee</h1>
     <br/>
     <p>This website programed by django drf for practice API web</p>
     <p>You can use these path's for using api's</p>
     <a href='api/v1/get-all-data/'>Get all Books (GET)</a><br/><br/>
     <a href='api/v1/get-fav-data/'>Get all favorite Books (GET)</a><br/><br/>
     <a href='api/v1/create-data/'>Create a Book with json data taken (POST)</a><br/><br/>
     <a href='api/v1/search/?name=پایتون&author=پایتون'>Search books for name or author contains `پایتون` </a><br/><br/>
     <a href='api/v1/detail-data/<1>/'>Show Book detail with `1` id (GET)</a><br/><br/>
     <a href='api/v1/detail-data/<1>/'>Delete a Book with `1` id (DELETE)</a><br/><br/>
     <a href='api/v1/detail-data/<1>/'>Update a Book with `1` id (PUT)</a><br/><br/>
     <a href='api/v1/get-all-data/'>Get all Books(GET)</a><br/><br/>
     <br><hr><br>
     
   </center>    
     <h1>Correct json data</h1>
   <pre style='text-align: left;'>
        {
            "name": "ترفند های پایتون",
            "author": "محمد بابازاده",
            "desc": "این کتاب ترجمه نشده است",
            "fav": true, 
        }
    </pre><br><br>
    </div>
    
        name:string(max_length=50, required)<br>
        author:string(max_length=50, required)<br>
        desc:string(required)<br>
        fav:bool(default=False)<br>
        image:File(default=null/None)<br>
    </pre>

  '''
    return HttpResponse(html)
