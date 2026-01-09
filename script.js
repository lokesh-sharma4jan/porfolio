// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  });
});

// Navbar scroll effect
const navbar = document.querySelector(".navbar");
const navLinks = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", () => {
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }

  // Active nav link on scroll
  let current = "";
  const sections = document.querySelectorAll(".section, .hero");

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (scrollY >= sectionTop - 200) {
      current = section.getAttribute("id");
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove("active");
    if (link.getAttribute("href") === `#${current}`) {
      link.classList.add("active");
    }
  });
});

// Mobile menu toggle
const hamburger = document.querySelector(".hamburger");
const navLinksContainer = document.querySelector(".nav-links");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navLinksContainer.classList.toggle("active");
});

// Close mobile menu when clicking on a link
navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navLinksContainer.classList.remove("active");
  });
});

// Typing effect for hero section
const roles = [
  "Senior Backend Engineer",
  "Distributed Systems Architect",
  "Microservices Expert",
  "Cloud-Native Developer",
  "System Design Specialist",
  "Performance Engineer",
];
let roleIndex = 0;
let charIndex = 0;
let isDeleting = false;
const typingSpeed = 100;
const deletingSpeed = 50;
const pauseTime = 2000;

function typeRole() {
  const typedRoleElement = document.querySelector(".typed-role");
  if (!typedRoleElement) return;

  const currentRole = roles[roleIndex];

  if (isDeleting) {
    typedRoleElement.textContent = currentRole.substring(0, charIndex - 1);
    charIndex--;
  } else {
    typedRoleElement.textContent = currentRole.substring(0, charIndex + 1);
    charIndex++;
  }

  let typeSpeed = isDeleting ? deletingSpeed : typingSpeed;

  if (!isDeleting && charIndex === currentRole.length) {
    typeSpeed = pauseTime;
    isDeleting = true;
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    roleIndex = (roleIndex + 1) % roles.length;
  }

  setTimeout(typeRole, typeSpeed);
}

// Start typing effect when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", typeRole);
} else {
  typeRole();
}

// Counter animation for stats
const counters = document.querySelectorAll(".counter");
const observerOptions = {
  threshold: 0.5,
  rootMargin: "0px",
};

const counterObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const counter = entry.target;
      const target = parseInt(counter.getAttribute("data-target"));
      const duration = 2000;
      const increment = target / (duration / 16);
      let current = 0;

      const updateCounter = () => {
        current += increment;
        if (current < target) {
          counter.textContent = Math.floor(current);
          requestAnimationFrame(updateCounter);
        } else {
          counter.textContent = target;
        }
      };

      updateCounter();
      observer.unobserve(counter);
    }
  });
}, observerOptions);

counters.forEach((counter) => {
  counterObserver.observe(counter);
});

// Skill bars animation
const skillBars = document.querySelectorAll(".skill-progress");

const skillObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const progress = entry.target.getAttribute("data-progress");
      entry.target.style.width = progress + "%";
      skillObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

skillBars.forEach((bar) => {
  skillObserver.observe(bar);
});

// Scroll animations for sections
const sections = document.querySelectorAll(".section");

const sectionObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("fade-in-up");
        sectionObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.1,
  }
);

sections.forEach((section) => {
  sectionObserver.observe(section);
});

// Back to top button
const backToTopBtn = document.getElementById("backToTop");

window.addEventListener("scroll", () => {
  if (window.scrollY > 500) {
    backToTopBtn.classList.add("visible");
  } else {
    backToTopBtn.classList.remove("visible");
  }
});

backToTopBtn.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});

// Contact form submission
const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", (e) => {
  e.preventDefault();

  // Get form data
  const formData = new FormData(contactForm);
  const data = Object.fromEntries(formData);

  // Here you would typically send the data to a server
  console.log("Form submitted:", data);

  // Show success message
  alert("Thank you for your message! I will get back to you soon.");

  // Reset form
  contactForm.reset();
});

// Particles effect for hero section (optional enhancement)
function createParticle() {
  const hero = document.querySelector(".hero");
  const particle = document.createElement("div");
  particle.className = "particle";
  particle.style.cssText = `
        position: absolute;
        width: 5px;
        height: 5px;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        pointer-events: none;
        animation: particleFloat 4s linear infinite;
    `;

  particle.style.left = Math.random() * 100 + "%";
  particle.style.animationDelay = Math.random() * 4 + "s";

  hero.appendChild(particle);

  setTimeout(() => {
    particle.remove();
  }, 4000);
}

// Add particle animation CSS
const style = document.createElement("style");
style.textContent = `
    @keyframes particleFloat {
        0% {
            transform: translateY(100vh) scale(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) scale(1);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Create particles periodically
setInterval(createParticle, 500);

// Project card hover effects
const projectCards = document.querySelectorAll(".project-card");

projectCards.forEach((card) => {
  card.addEventListener("mouseenter", function () {
    this.style.transform = "translateY(-10px) scale(1.02)";
  });

  card.addEventListener("mouseleave", function () {
    this.style.transform = "translateY(0) scale(1)";
  });
});

// Timeline items animation
const timelineItems = document.querySelectorAll(".timeline-item");

const timelineObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "translateX(0)";
        }, index * 200);
        timelineObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.2,
  }
);

timelineItems.forEach((item) => {
  item.style.opacity = "0";
  item.style.transform = "translateX(-50px)";
  item.style.transition = "all 0.6s ease";
  timelineObserver.observe(item);
});

// Education cards animation
const educationCards = document.querySelectorAll(".education-card");

educationCards.forEach((card, index) => {
  card.style.opacity = "0";
  card.style.transform = "translateY(30px)";
  card.style.transition = "all 0.6s ease";

  const cardObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.style.opacity = "1";
            entry.target.style.transform = "translateY(0)";
          }, index * 150);
          cardObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  cardObserver.observe(card);
});

// Preload images
window.addEventListener("load", () => {
  const images = document.querySelectorAll("img");
  images.forEach((img) => {
    if (img.complete) {
      img.classList.add("loaded");
    } else {
      img.addEventListener("load", () => {
        img.classList.add("loaded");
      });
    }
  });
});

// Add cursor trail effect (optional)
let cursorTrail = [];
const trailLength = 10;

document.addEventListener("mousemove", (e) => {
  cursorTrail.push({ x: e.clientX, y: e.clientY });

  if (cursorTrail.length > trailLength) {
    cursorTrail.shift();
  }
});

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Add scroll progress indicator
const createScrollProgress = () => {
  const progressBar = document.createElement("div");
  progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        width: 0%;
        z-index: 9999;
        transition: width 0.1s ease;
    `;
  document.body.appendChild(progressBar);

  window.addEventListener(
    "scroll",
    debounce(() => {
      const windowHeight =
        document.documentElement.scrollHeight -
        document.documentElement.clientHeight;
      const scrolled = (window.scrollY / windowHeight) * 100;
      progressBar.style.width = scrolled + "%";
    }, 10)
  );
};

createScrollProgress();

// Add keyboard navigation
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    hamburger.classList.remove("active");
    navLinksContainer.classList.remove("active");
  }
});

// Form validation enhancement
const formInputs = document.querySelectorAll(
  ".contact-form input, .contact-form textarea"
);

formInputs.forEach((input) => {
  input.addEventListener("blur", function () {
    if (this.value.trim() === "") {
      this.style.borderColor = "red";
    } else {
      this.style.borderColor = "";
    }
  });

  input.addEventListener("focus", function () {
    this.style.borderColor = "";
  });
});

// Professional Scroll Reveal Animation
const scrollRevealOptions = {
  threshold: 0.15,
  rootMargin: "0px 0px -50px 0px",
};

const scrollRevealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = "1";
      entry.target.style.transform = "translateY(0)";
      scrollRevealObserver.unobserve(entry.target);
    }
  });
}, scrollRevealOptions);

// Observe all sections and cards for scroll reveal
document
  .querySelectorAll(
    ".section, .project-card, .skill-category, .timeline-item, .education-card"
  )
  .forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(30px)";
    el.style.transition = "opacity 0.6s ease-out, transform 0.6s ease-out";
    scrollRevealObserver.observe(el);
  }); // Enhanced typing effect with more professional roles
const typingElement = document.querySelector(".typed-role");
if (typingElement) {
  typingElement.style.display = "inline-block";
  typingElement.style.minWidth = "250px";
}

// Smooth anchor scrolling with offset for fixed navbar
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      const offsetTop = target.offsetTop - 80;
      window.scrollTo({
        top: offsetTop,
        behavior: "smooth",
      });
    }
  });
});

// Add loading state removal
window.addEventListener("load", () => {
  document.body.classList.remove("loading");
});

// Professional console message
console.log(
  "%c🚀 Portfolio Website Loaded Successfully!",
  "color: #4F46E5; font-size: 16px; font-weight: bold;"
);
console.log(
  "%c💼 Lokesh Babu Sharma | Senior Java Developer",
  "color: #7C3AED; font-size: 14px;"
);
console.log(
  "%c✉️ luckysharma824@gmail.com",
  "color: #6B7280; font-size: 12px;"
);
