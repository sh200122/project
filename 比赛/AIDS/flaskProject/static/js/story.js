var swiper = new Swiper('.swiper-container', {
  slidesPerView: 3,
  spaceBetween: 50,
  centeredSlides: true, // 确保当前活跃的幻灯片始终居中
  loop: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  speed: 800,
});


// 输入内容不能为空,清除,提交后感谢，ajax前后端
document.getElementById('submitBtn').addEventListener('click', function () {
  var textarea = document.getElementById('floatingTextarea2');
  var feedback = document.getElementById('inputFeedback');

  if (textarea.value.trim() === "") {
    textarea.classList.add('is-invalid');
    feedback.style.display = 'block';
  } else {
    textarea.classList.remove('is-invalid');
    feedback.style.display = 'none';

    var data = {
      user_id: '1', // 替换为实际的用户ID
      content: textarea.value.trim()
    };

    fetch('/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          alert(data.error);
        } else {
          alert(data.message);
        }
      })
      .catch(error => console.error('Error:', error));
    // 显示Toast
    var toast = new bootstrap.Toast(document.getElementById('thankYouToast'));
    toast.show();

    // 清除输入框内容
    textarea.value = '';

    // 隐藏Modal
    var modal = bootstrap.Modal.getInstance(document.getElementById('myModal'));
    modal.hide();
  }

});

document.getElementById('floatingTextarea2').addEventListener('input', function () {
  var textarea = document.getElementById('floatingTextarea2');
  var feedback = document.getElementById('inputFeedback');

  if (textarea.value.trim() !== "") {
    textarea.classList.remove('is-invalid');
    feedback.style.display = 'none';
  }
});

document.getElementById('myModal').addEventListener('hidden.bs.modal', function () {
  clearInput();
});

function clearInput() {
  var textarea = document.getElementById('floatingTextarea2');
  var feedback = document.getElementById('inputFeedback');

  textarea.value = "";
  textarea.classList.remove('is-invalid');
  feedback.style.display = 'none';
}

// 防抖
document.getElementById('myModal').addEventListener('show.bs.modal', function () {
  document.body.style.overflow = 'hidden';
});

document.getElementById('myModal').addEventListener('hidden.bs.modal', function () {
  document.body.style.overflow = 'auto';
});
