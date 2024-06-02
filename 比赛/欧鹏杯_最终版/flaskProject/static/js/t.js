var temp=0;

var flage=true;

var v = function (i){
    if(flage){
        flage = false;
        var t = 500;

        var v = $('.wrapper > .img > .card:not(:eq('+i+'))');
        var s = $('.wrapper > .img > .card:eq('+i+')');
        // var bv = $('.wrapper > .Button li:not(:eq('+i+'))');
        // var bs = $('.wrapper > .Button li:eq('+i+')');

        // bv.animate({
        //     'left':'10em'
        // },t);
        // bs.animate({
        //     'left':'00em'
        // },t);
        
        
        v.css({        'z-index':'1','left':'-100%'    });

        s.css({        'z-index':'2'    });

        s.animate({
            'left':'0%'
        },t);
        
        setTimeout(function(){
            $('.wrapper > .img').css({     'background-image':s.css("background-image")})
            flage = true;
        },t+5)
        
    }
    
}
var L = function(){
    if (temp>4) {
        temp=0;
    }
    else{
        temp++;
    }
    // v(temp);
    console.log('L');
}

var ref = setInterval(L(),13000);

$('.Button > li').mousedown(function () { 
    temp=$(this).index();
    // clearInterval(ref);
    if (flage) {
        $(this).prevAll().find('a').css({
            'background-color':'rgba(0, 0, 0, 0.37)'
        });   
        $(this).find('a').css({
            'background-color':'rgba(0, 0, 0, 0)'
        });
        $(this).nextAll().find('a').css({
            'background-color':'rgba(0, 0, 0, 0.37)'
        }); 
        v(temp);
        console.log('D');
    }
    // ref = setInterval(L(),13000);
 });
 $('.Button > li').mouseenter(function(){
    clearInterval(ref);

    var t = 100;
    var i = $(this).index();
})
$('.wrapper').mouseenter(function(){
    clearInterval(ref);
})
$('.wrapper').mouseout(function(){
    ref = setInterval(L(),13000);
})

$('.end').parent().css({'box-shadow':' 0 0px 5px #00000056'})
