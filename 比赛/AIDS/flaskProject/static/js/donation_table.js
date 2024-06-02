//选项卡
window.onload = function () {
    var item = document.getElementsByClassName("item");
    var it = item[0].getElementsByTagName("div");

    var content = document.getElementsByClassName("content");
    var con = content[0].getElementsByTagName("div");

    for (let i = 0; i < it.length; i++) {
        it[i].onclick = function () {
            for (let j = 0; j < it.length; j++) {
                it[j].className = '';
                con[j].style.display = "none";
            }
            this.className = "active";
            it[i].index = i;
            con[i].style.display = "block";
        }
    }
}

//免责弹窗
function showPopup() {
    var overlay = document.getElementById("overlay");
    overlay.style.display = "block";
}
//取消
function hidePopup() {
    var overlay = document.getElementById("overlay");
    overlay.style.display = "none";
}

//点击捐款金额
document.getElementById('myButton1').addEventListener('click', function () {
    // 获取按钮的文本内容  
    var buttonText = this.textContent || this.innerText;
    // 获取输入框元素  
    var inputElement = document.getElementById('myInput');
    // 将按钮的文本内容设置到输入框的值中  
    inputElement.value = buttonText;
});
document.getElementById('myButton2').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton3').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton4').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton5').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton6').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton7').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton8').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton9').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton10').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton11').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});
document.getElementById('myButton12').addEventListener('click', function () {
    var buttonText = this.textContent || this.innerText;
    var inputElement = document.getElementById('myInput');
    inputElement.value = buttonText;
});


