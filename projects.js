const projects = [
  {
    id: "attendance-prediction",
    title: "Attendance Prediction ML Models",
    category: "Machine Learning",
    summary: "Machine learning models built in Databricks and Apache Spark to predict attendance for the 2016 baseball season.",
    outcome: "Best model reached roughly 83% accuracy and connected predictive work to profitability planning.",
    tags: ["Databricks", "Apache Spark", "Python", "Machine Learning"],
    icon: "Logos/databricks_logo.png",
    iconAlt: "Databricks logo",
    featured: true,
    links: [
      {
        label: "View Project",
        url: "Attendance_Prediction/Combined.html"
      }
    ]
  },
  {
    id: "inmates-reintegrate-database",
    title: "Inmates Reintegrate Program Database Design",
    category: "Database Design",
    summary: "Database design, development, and implementation for an inmate reintegration program.",
    outcome: "Modeled the data structure with draw.io and implemented the database using Microsoft SQL Server and Azure.",
    tags: ["SQL Server", "Azure", "ERD", "Data Modeling"],
    icon: "Logos/msSQLazure_logo.png",
    iconAlt: "Microsoft SQL Server and Azure logo",
    featured: true,
    links: [
      {
        label: "View on GitHub",
        url: "https://github.com/pzumbap/Database_design"
      }
    ]
  },
  {
    id: "intelligent-tourist-website",
    title: "Intelligent Tourist Website",
    category: "Web Analytics",
    summary: "A web application concept for suggesting tours and excursions based on solo traveler preferences.",
    outcome: "Combined HTML, CSS, JavaScript, Chart.js, and Python Flask into an interactive recommendation experience.",
    tags: ["Flask", "JavaScript", "Chart.js", "HTML/CSS"],
    icon: "Logos/html_css_js_logo.png",
    iconAlt: "HTML CSS and JavaScript logo",
    featured: true,
    links: [
      {
        label: "Visit Website",
        url: "http://shawnmurphy.myweb.usf.edu/Destinations2.html"
      },
      {
        label: "Video Walkthrough",
        url: "https://usfedu-my.sharepoint.com/personal/jennaptak_usf_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fjennaptak%5Fusf%5Fedu%2FDocuments%2FRecordings%2FAssignment%204%2D20221019%5F210600%2DMeeting%20Recording%2Emp4&ga=1"
      }
    ]
  },
  {
    id: "divorce-in-the-us",
    title: "Divorce in the US",
    category: "Analytics",
    summary: "A report exploring possible reasons and contributing factors for divorce in the United States.",
    outcome: "Used SQLite, RStudio, and Tableau to support analysis for psychology-focused decision making.",
    tags: ["SQLite", "R", "Tableau", "Reporting"],
    icon: "Logos/tableau.png",
    iconAlt: "Tableau logo",
    featured: true,
    links: [
      {
        label: "View Report",
        url: "Divorce_US/Project_Report.pdf"
      }
    ]
  }
];

const featuredProjects = document.querySelector("#featured-projects");
const projectGrid = document.querySelector("#project-grid");
const projectFilters = document.querySelector("#project-filters");
const projectSearch = document.querySelector("#project-search");
const projectCount = document.querySelector("#project-count");

let activeFilter = "All";

function isExternalLink(url) {
  return /^https?:\/\//.test(url);
}

function linkAttributes(url) {
  return isExternalLink(url) ? ' target="_blank" rel="noopener"' : "";
}

function renderFeaturedProjects() {
  featuredProjects.innerHTML = projects
    .filter((project) => project.featured)
    .map((project) => `
      <a class="topic-tile" href="#${project.id}">
        <span>${project.category}</span>
        <strong>${project.title}</strong>
      </a>
    `)
    .join("");
}

function renderFilters() {
  const categories = ["All", ...new Set(projects.map((project) => project.category))];

  projectFilters.innerHTML = categories
    .map((category) => `
      <button class="filter-button${category === activeFilter ? " is-active" : ""}" type="button" data-filter="${category}">
        ${category}
      </button>
    `)
    .join("");
}

function renderProjectCard(project) {
  const tags = project.tags.map((tag) => `<li>${tag}</li>`).join("");
  const links = project.links
    .map((link, index) => `
      <a class="project-link${index === 0 ? " primary" : ""}" href="${link.url}"${linkAttributes(link.url)}>
        ${link.label}
      </a>
    `)
    .join("");

  return `
    <article class="project-card" id="${project.id}">
      <div class="project-card-header">
        <div class="project-icon">
          <img src="${project.icon}" alt="${project.iconAlt}">
        </div>
        <div>
          <p class="project-category">${project.category}</p>
          <h3>${project.title}</h3>
        </div>
      </div>
      <div>
        <p class="project-summary">${project.summary}</p>
        <p class="project-outcome">${project.outcome}</p>
      </div>
      <div>
        <ul class="tag-list" aria-label="${project.title} technologies">${tags}</ul>
        <div class="project-links">${links}</div>
      </div>
    </article>
  `;
}

function projectMatchesSearch(project, searchTerm) {
  const searchableText = [
    project.title,
    project.category,
    project.summary,
    project.outcome,
    ...project.tags
  ].join(" ").toLowerCase();

  return searchableText.includes(searchTerm);
}

function renderProjects() {
  const searchTerm = projectSearch.value.trim().toLowerCase();
  const filteredProjects = projects.filter((project) => {
    const matchesFilter = activeFilter === "All" || project.category === activeFilter;
    const matchesSearch = projectMatchesSearch(project, searchTerm);
    return matchesFilter && matchesSearch;
  });

  projectCount.textContent = `${filteredProjects.length} project${filteredProjects.length === 1 ? "" : "s"}`;

  projectGrid.innerHTML = filteredProjects.length
    ? filteredProjects.map(renderProjectCard).join("")
    : '<p class="empty-state">No projects match that search.</p>';
}

projectFilters.addEventListener("click", (event) => {
  const button = event.target.closest("button");

  if (!button) {
    return;
  }

  activeFilter = button.dataset.filter;
  renderFilters();
  renderProjects();
});

projectSearch.addEventListener("input", renderProjects);

renderFeaturedProjects();
renderFilters();
renderProjects();
