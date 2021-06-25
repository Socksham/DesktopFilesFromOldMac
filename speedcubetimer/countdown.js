function countdown(){
    var timer = document.getElementById('timer');
    var counter = 16;
    
    var interval2 = setInterval(inter, 1000);
    
    function inter(){
        counter -= 1;
        timer.textContent = counter;
        if(counter < 1){
            timer.textContent = 'DNF';
        }
    }

    this.stopCountdown = function(){
        clearInterval(interval2);
    }
}


