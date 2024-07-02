import streamlit as st

def render_navbar():
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown("""
    <head>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #92C5E8; height:80px; margin-top: 40px; margin-bottom: 20px;">
        <div class="container-fluid">
            <img src= "https://i.im.ge/2024/03/11/RSYRrJ.Screenshot-2024-03-11-at-7-23-37-PM.png" alt="Logo" style="height: 75px; width: auto; margin-right: 20px; margin-top: 10px; margin-bottom: 5px">
            <a class="nav-link" href="#" style="color: black;">Men</a>
            <a class="nav-link" href="#" style="color: black;">Women</a>
            <a class="nav-link" href="#" style="color: black;">Children</a>
            <div class="input-group" style="margin-right: 20px;">
                <input type="text" class="form-control" placeholder="Search" aria-label="Search" aria-describedby="button-addon2">
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
                </div>
            </div>
            <div class="navbar-collapse justify-content-end">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="#" style="color: black;"><i class="fa fa-user" aria-hidden="true"></i> Profile</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" style="color: black;"><i class="fa fa-heart" aria-hidden="true"></i> Wishlist</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" style="color: black;"><i class="fa fa-shopping-bag" aria-hidden="true"></i> Bag</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)


def render_navbar2():
    # Adding Bootstrap CSS
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    # Adding custom CSS for navbar
    st.markdown("""
        <style>
            .navbar {
                background: black;
                font-family: Arial, sans-serif; /* Custom font style */
            }
            .navbar-brand {
                color: white !important; /* Setting text color to white */
                font-size: 24px; /* Custom font size */
                # font-weight: bold; /* Custom font weight */
                text-decoration: none; /* Remove underline */
                font-family: Georgia;
                display: flex;
                align-items: center
                
            }
            .navbar-button {
                background-color: white !important;
                color: red !important;
                border: 1px solid red;
            }
            .navbar-button:hover {
                background-color: red !important;
                color: white !important;
            }
        </style>
        """, unsafe_allow_html=True)

    # Navbar content
    st.markdown("""
        <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="margin-top: 50px; margin-bottom: 0px;">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Coach</a>
                
                   
                
            
        </nav>
        """, unsafe_allow_html=True)


