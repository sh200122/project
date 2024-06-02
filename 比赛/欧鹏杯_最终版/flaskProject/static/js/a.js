// var a = function(){
//     alert('aca')
// }
var flage = '+';
var aj1 = '<svg t="1716020387843" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2405" width="48" height="48"><path d="M426.666667 426.666667H85.546667A85.418667 85.418667 0 0 0 0 512c0 47.445333 38.314667 85.333333 85.546667 85.333333H426.666667v341.12c0 47.274667 38.186667 85.546667 85.333333 85.546667 47.445333 0 85.333333-38.314667 85.333333-85.546667V597.333333h341.12A85.418667 85.418667 0 0 0 1024 512c0-47.445333-38.314667-85.333333-85.546667-85.333333H597.333333V85.546667A85.418667 85.418667 0 0 0 512 0c-47.445333 0-85.333333 38.314667-85.333333 85.546667V426.666667z" fill="#b12e31" p-id="2406"></path></svg>'
$('.im > .tak ').click(function (e) { 
    // e.preventDefault();
    // this.toValue(8415)
    console.log($(this).index())
    // alert()
    if(flage == '+'){
        flage = '-';
        $(this).find('.jia').hide ();
        $(this).find('.jian').show ();
        $(this).next().show();
    }
    else{
        flage = '+';
        $(this).find('.jia').show ();
        $(this).find('.jian').hide();
        $(this).next().hide();
    }
});