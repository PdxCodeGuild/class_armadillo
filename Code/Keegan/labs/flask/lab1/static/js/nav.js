document.addEventListener('DOMContentLoaded', () => {
    let mainContent = document.querySelector('#main-container');
    let toggle = document.querySelector('.toggle');
    let navbar = document.querySelector('.navbar');
    let navbarHide = '-80vw';
    let navbarShow = '0px';

    // if the navbar's left attribute is an empty string,
    // as it is by default, set it to 0px
    if(navbar.style.left == '' && window.innerWidth < 992){
        if(window.innerWidth < 992){
            navbar.style.left = navbarHide;
        } else {
            navbar.style.left = navbarShow;
        }
    } 

    window.addEventListener('resize', () => {
        if(window.innerWidth < 992){
            navbar.style.left = navbarHide;
        } else {
            navbar.style.left = navbarShow;
        }
    });

    mainContent.addEventListener('click', e => {
        // if clicked object isn't the toggle button or one of its lines
        // and if it the clicked object isn't the navbar, hide the nav if shown
        if(window.innerWidth < 992){
            if(e.target.id != 'toggle' && !e.target.classList.contains('line') && e.target != navbar){
                if(navbar.style.left == navbarShow){
                    navbar.style.left = navbarHide;
                }
            }
        }


        // if the toggle or one of its lines are clicked,
        // toggle the nav depending on its state
        if (e.target.id == 'toggle' || e.target.classList.contains('line')){
            if(navbar.style.left == navbarShow){
                navbar.style.left = navbarHide;

            } else if (navbar.style.left == navbarHide){
                navbar.style.left = navbarShow;
            }
        }   
    });
});