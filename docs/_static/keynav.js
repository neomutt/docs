document.addEventListener("keydown", (e) => {
  // Ignore interactive elements and modifier keys
  if (e.target.closest('input, textarea, select, [contenteditable], [role="textbox"]')) return;
  if (e.altKey || e.ctrlKey || e.metaKey) return;
  if (e.repeat) return;

  const key = e.key;
  const pagename = document.querySelector('meta[name="doc-pagename"]')?.content;
  const docRoot = document.querySelector('meta[name="doc-root"]')?.content;
  if (!pagename) return;

  function go(relativePath) {
    window.location.href = new URL(relativePath, window.location.href).href;
  }

  // Previous page
  if (key === "ArrowLeft") {
    const link = document.querySelector('a[rel="prev"], a.prev-page') || document.querySelector('link[rel="prev"]');
    if (link) window.location.href = link.href;

  // Next page
  } else if (key === "ArrowRight") {
    const link = document.querySelector('a[rel="next"], a.next-page') || document.querySelector('link[rel="next"]');
    if (link) window.location.href = link.href;

  // Parent page (via breadcrumbs)
  } else if (key === "u") {
    if (pagename === "index") return;
    const crumbs = document.querySelectorAll(".bd-breadcrumbs .breadcrumb-item:not(.active) a.nav-link");
    const parent = crumbs.length ? crumbs[crumbs.length - 1] : null;
    if (parent) window.location.href = parent.href;

  // Section root
  } else if (key === "U" && docRoot) {
    if (!pagename.includes("/") || pagename === "index") return;
    const section = pagename.split("/")[0];
    if (pagename === section + "/index") return;
    go(docRoot + section + "/index.html");

  // Diátaxis section keys
  } else if (docRoot) {
    const sections = { t: "tutorials", h: "howto", e: "explanation", r: "reference" };
    const section = sections[key];
    if (section) go(docRoot + section + "/index.html");
  }
});
