from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Document</title>
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        .icon {
            color: #cc324b;
            font-size: 25px;
            padding: 5px;
        }
        i:hover {
            color:gray;
        }
        .bgc{
            background-color: gainsboro;
        }
    </style>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
   
</head>
<body>
  
    <div class="row border border-3 bgc">
        <div class="col-4 bgc">
            <i class="bi bi-twitter icon"></i>
            <i class="bi bi-youtube icon"></i>
            <i class="bi bi-facebook icon"></i>
            <i class="bi bi-linkedin icon"></i>
            <i class="bi bi-pinterest icon"></i>
            <i class="bi bi-whatsapp icon"></i>
            <i class="bi bi-instagram icon"></i>
            <p>
              <a href="https://saveetha.ac.in/"></br>
                <img src="WEB_LOGO-01.png" height="50px" alt="Saveetha logo" /><br /> </a></p>
        </div>
        

        <div class="col-5">
            <nav class="navbar navbar-expand-lg bgc">
                <div class="container-fluid">
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNavDropdown">
                    <ul class="navbar-nav">
                      <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Alumini<i class="bi bi-three-dots-vertical"></i></a>
    
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="#">Events<i class="bi bi-three-dots-vertical"></i></a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="#">Career<i class="bi bi-three-dots-vertical"></i></a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="#">Login<i class="bi bi-three-dots-vertical"></i></a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="#">SEC portal</a>
                      </li>              
                    </ul>
                  </div>
                </div>
              </nav>
              </div>
            
            
            <div class="row-1 bgc">
            <nav class="navbar navbar-expand-lg bgc">
                <div class="container-fluid">
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="navbarNavDropdown">
                    <ul class="navbar-nav">
                      <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home  </a>
    
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" href="#">About  </a>
                      </li>
                      <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                          Department
                        </a>
                        <ul class="dropdown-menu">
                          <li><a class="dropdown-item" href="#">Information Technology</a></li>
                          <li><a class="dropdown-item" href="#">Computer Science and Engineering</a></li>
                          <li><hr class="dropdown-divider"></li>
                          <li><a class="dropdown-item" href="#">Electrical and Electronics Engineering</a></li>
                          <li><a class="dropdown-item" href="#">Electronics and Communication Engineering</a></li>
                        </ul>
                        <li class="nav-item dropdown">
                          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Life at SEC
                          </a>
                          <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#"> Academic Life<i class="bi bi-three-dots-vertical"></i></a></li>
                            <li><a class="dropdown-item" href="#">Student Life<i class="bi bi-three-dots-vertical"></i></a></li>
                          </ul>
                          <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                              Admissions
                            </a>
                            <ul class="dropdown-menu">
                              <li><a class="dropdown-item" href="#"> Admission Procedure<i class="bi bi-three-dots-vertical"></i></a></li>
                              <li><a class="dropdown-item" href="#">Offered Course<i class="bi bi-three-dots-vertical"></i></a></li>
                            </ul>
                      </li>
                    </ul>
                  </div>
                </div>
              </nav>
            </div>
           
            
            <div class="row-3">
            <div style="display:flex;">
              <div style="width:30%;">
                <h1>Admission Enquiry</h1><br />
                <h2>Chat with Student Ambassador </h2>
                <h3>BLOGS</h3>
              </div>
              <div style="width:70%;">
          
          <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel" data-bs-interval="2000">
      
              <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
              </div>
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="1.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="2.jpg" class="d-block w-100" al  t="...">
                </div>
                <div class="carousel-item">
                  <img src="3..jpeg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="4.png" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="7.png" class="d-block w-100" alt="...">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
          </div>
          <div class="col-3 bgc">
            <div class="border border-2">
            <i class="bi bi-search"></i>
            <input typle="text" class="bgc border-0"/>
          </div>
            
            
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
            
</body>

</html>
"""
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)

print("my webserver is running...")
httpd.serve_forever()