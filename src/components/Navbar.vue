<template>
  <header class="nav">
    <nav class="navbar navbar-expand-md w-100 wave-bg-blue bsb-navbar bsb-navbar-hover bsb-navbar-caret">
      <div class="container">
        <a class="navbar-brand" href="index.html">
         <h1>Merlion Tours</h1> 
        </a>
        <button class="navbar-toggler border-0" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
          
        </button>
        <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
          <div class="offcanvas-header">
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <ul id="bsb-tpl-navbar" class="navbar-nav justify-content-end flex-grow-1">
              <li class="nav-item">
                <a class="nav-link" href="/">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/about" >About Us</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  For Tourists
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                  <a class="dropdown-item" href="/tourlisting">Tour Listings</a>
                </div>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    For Guides
                  </a>
                  <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                    <a class="dropdown-item" href="/public/jobportal.html">Job Portal</a>
                    <a class="dropdown-item" href="#">FAQ</a>
                  </div>
                  <li class="nav-item">
                    <a class="nav-link" href="/enquiry" >Enquire Us</a>
                  </li>
                </li>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style>
  /* @media (min-width: 768px) {
    .bd-placeholder-img-lg {
      font-size: 3.5rem;
    }
    
  }

  .form-control-dark {
  border-color: var(--bs-gray);
  }
  .form-control-dark:focus {
    border-color: #fff;
    box-shadow: 0 0 0 .25rem rgba(255, 255, 255, .25);
  } */
        
</style>

