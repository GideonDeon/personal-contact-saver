let form = document.getElementsByTagName('input')
let show = document.getElementById('check')
function text(){
    form[2].type === 'text'
}text()
function passWord(){
    if(form[2].type === 'password'){
        form[2].type = 'text'
    }
    else{
        form[2].type = 'password'
    }
}
