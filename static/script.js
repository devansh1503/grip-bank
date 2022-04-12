var a = document.getElementsByClassName('home')[0];
var b = document.getElementsByClassName('cos')[0];
var c = document.getElementsByClassName('tra')[0];
var d = document.getElementsByClassName('his')[0];
var curr = a;
function newPage(i){
    switch(i){
        case 1: curr.classList.add('hide');
        a.classList.remove('hide');
        curr = a; break;
        case 2: curr.classList.add('hide');
        b.classList.remove('hide');
        curr = b; break;
        case 3:curr.classList.add('hide');
        c.classList.remove('hide');
        curr = c; break;
        case 4:curr.classList.add('hide');
        d.classList.remove('hide');
        curr = d; break;
        

    }
}