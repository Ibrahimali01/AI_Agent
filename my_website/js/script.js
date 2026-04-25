// بيانات المشاريع
const projects = [
    {
        title: "محرك بحث ذكي",
        description: "محرك بحث متقدم باستخدام تقنيات الذكاء الاصطناعي لتحسين نتائج البحث",
        tags: ["Python", "AI", "API"],
        status: "قيد التطوير"
    },
    {
        title: "مدونة شخصية",
        description: "منصة مدونة تفاعلية مع نظام إدارة محتوى متكامل",
        tags: ["HTML", "CSS", "JavaScript"],
        status: "مكتمل"
    },
    {
        title: "منصة تعليمية",
        description: "منصة لتعليم البرمجة بلغة بايثون للمبتدئين",
        tags: ["Python", "Web", "Education"],
        status: "مكتمل"
    },
    {
        title: "أداة تحليل بيانات",
        description: "أداة لتحليل البيانات وتوليد التقارير الإحصائية",
        tags: ["Python", "Data", "Analytics"],
        status: "قيد التطوير"
    }
];

// تهيئة الموقع
document.addEventListener('DOMContentLoaded', function() {
    loadProjects();
    startLearningCounter();
    addScrollAnimations();
});

// تحميل المشاريع
function loadProjects() {
    const container = document.getElementById('projects-container');
    
    projects.forEach(project => {
        const card = document.createElement('div');
        card.className = 'project-card';
        card.innerHTML = `
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <div class="tags" style="margin-top: 1rem;">
                ${project.tags.map(tag => `<span style="display: inline-block; background: #667eea; color: white; padding: 4px 8px; border-radius: 4px; margin: 2px; font-size: 0.9rem;">${tag}</span>`).join('')}
            </div>
            <div style="margin-top: 1rem; font-weight: bold; color: ${project.status === 'مكتمل' ? '#4CAF50' : '#FF9800'};">
                ${project.status}
            </div>
        `;
        container.appendChild(card);
    });
}

// عداد أيام التعلم
function startLearningCounter() {
    const startDate = new Date('2024-01-01');
    const counter = document.getElementById('days-counter');
    
    function updateCounter() {
        const today = new Date();
        const diffTime = Math.abs(today - startDate);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        counter.textContent = diffDays;
    }
    
    updateCounter();
    setInterval(updateCounter, 86400000); // تحديث كل 24 ساعة
}

// رسالة ترحيبية
function showMessage() {
    const messages = [
        "أهلاً بك في رحلة تعلم البرمجة!",
        "كل خطوة صغيرة تقربك من هدفك!",
        "البرمجة فن يتطلب الصبر والممارسة!",
        "استمر في التعلم، النجاح قادم!",
        "أنت قادر على إنجاز أي شيء!"
    ];
    
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    alert(randomMessage);
}

// معالجة النموذج
function handleSubmit(event) {
    event.preventDefault();
    
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        message: document.getElementById('message').value,
        timestamp: new Date().toISOString()
    };
    
    // حفظ الرسالة (محلياً)
    let messages = JSON.parse(localStorage.getItem('contactMessages') || '[]');
    messages.push(formData);
    localStorage.setItem('contactMessages', JSON.stringify(messages));
    
    alert('شكراً لرسالتك! تم استلامها بنجاح.');
    event.target.reset();
    
    console.log('Message received:', formData);
}

// إضافة تأثيرات التمرير
function addScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.skill-card, .project-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s, transform 0.6s';
        observer.observe(card);
    });
}

// ميزة البحث الذكي
function smartSearch(query) {
    const allText = document.body.innerText.toLowerCase();
    return allText.includes(query.toLowerCase());
}

// تحميل محتوى ديناميكي
async function loadDynamicContent() {
    try {
        // محاكاة تحميل بيانات خارجية
        const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=3');
        const posts = await response.json();
        
        console.log('Dynamic content loaded:', posts);
    } catch (error) {
        console.log('Using local content instead');
    }
}

// بدء الموقع
loadDynamicContent();

// ميزة الوضع الليلي
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

// إدارة الذاكرة المحلية لمتابعة التقدم
function saveProgress() {
    const progress = {
        lastVisit: new Date().toISOString(),
        pagesVisited: JSON.parse(localStorage.getItem('pagesVisited') || '[]')
    };
    
    const currentPage = window.location.hash || '#home';
    if (!progress.pagesVisited.includes(currentPage)) {
        progress.pagesVisited.push(currentPage);
    }
    
    localStorage.setItem('pagesVisited', JSON.stringify(progress.pagesVisited));
    localStorage.setItem('lastProgress', JSON.stringify(progress));
}

// حفظ التقدم عند تغيير الصفحة
window.addEventListener('hashchange', saveProgress);
saveProgress();
