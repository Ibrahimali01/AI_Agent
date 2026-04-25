// تفاعلات بسيطة
document.addEventListener('DOMContentLoaded', function() {
    // تغيير حالة الإعجاب
    const likeButtons = document.querySelectorAll('.action:first-child');
    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const likesElement = this.closest('.post').querySelector('.likes');
            let likesCount = parseInt(likesElement.textContent.match(/\d+/)[0]);
            if (this.classList.contains('liked')) {
                this.classList.remove('liked');
                this.innerHTML = '<i class="fas fa-thumbs-up"></i> إعجاب';
                likesCount--;
            } else {
                this.classList.add('liked');
                this.innerHTML = '<i class="fas fa-thumbs-up" style="color:#1877f2;"></i> إعجاب';
                likesCount++;
            }
            likesElement.innerHTML = `<i class="fas fa-thumbs-up"></i> ${likesCount}`;
        });
    });

    // محاكاة إرسال منشور
    const postInput = document.querySelector('.post-header input');
    const createPostButton = document.querySelector('.post-options .option:first-child');
    if (createPostButton) {
        createPostButton.addEventListener('click', function() {
            if (postInput.value.trim() !== '') {
                alert('تم نشر المنشور: ' + postInput.value);
                postInput.value = '';
            }
        });
    }
});
