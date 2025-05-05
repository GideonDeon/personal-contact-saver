//show more details
var cont = true
$('main').on({dblclick:function(){
    if(cont){
        $(this).animate({
            height: "115vh"
        }, 500, function(){
            cont = false
        })
      

    }
   else{
        $(this).animate({
            height: "4em"
        }, 500, function(){
            cont = true
        })
   }
}})
$('main').on({taphold:function(){
        if(cont){
            $(this).animate({
                height: "115vh"
            }, 500, function(){
                cont = false
            })
          
    
        }
       else{
            $(this).animate({
                height: "4em"
            }, 500, function(){
                cont = true
            })
       }
    }})
$('#change').click(()=>{
    $('.colors').css('display', 'grid')
})
// settings
var show = true
$('.seticon').click(()=>{
    if(show){
        $('.settings').animate({
            width: '20%',
            padding:'10px'
        }, 150, ()=>{
            show = false
        })
    }
    else{
        $('.settings').animate({
            width: '0',
            padding:'0'
        }, 150, ()=>{
            show = true
        })
        $('.colors').css('display', 'none')
    }
})
time

function time(){
    let date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let session = 'AM';
    if(hh>=12){
        session='PM'
    }
    hh = (hh<10)? "0" + hh : hh;
    mm = (mm<10)? "0" + mm : mm;
    let display = `${hh}:${mm}`
    document.getElementById("clock").innerHTML = display;
    let sess = `${session}`
    document.getElementById("session").innerHTML = sess
}time()

//change theme

const element = document.querySelectorAll('.col')
const list  = []

document.body.classList.add(localStorage.getItem('color'));

element.forEach(e =>{
    list.push(e.getAttribute('data-color'));

    e.addEventListener('click', function(){
        document.body.classList.remove(...list);
        document.body.classList.add(this.getAttribute('data-color'));
        localStorage.setItem('color', this.getAttribute('data-color'));
    });
})
