document.addEventListener('DOMContentLoaded', () => {
  console.log('Site loaded');
  document.querySelectorAll('nav a').forEach(a => {
    a.addEventListener('click', (e) => {
      document.querySelectorAll('main > section').forEach(s => s.style.display = 'none');
      const target = document.getElementById(a.getAttribute('href').slice(1));
      if (target) target.style.display = 'block';
    });
  });
});