window.addEventListener("DOMContentLoaded", () => {
  const pageName = window.DOCUMENTATION_OPTIONS?.pagename;
  const isSearchPage =
    pageName === "search" || window.location.pathname.endsWith("/search.html");

  if (!isSearchPage) {
    return;
  }

  const searchResults = document.getElementById("search-results");
  const searchInput = document.querySelector('form.bd-search input[name="q"]');
  const query = new URLSearchParams(window.location.search).get("q")?.trim() ?? "";

  if (searchInput && query) {
    searchInput.value = query;
  }

  if (!searchResults || !query) {
    return;
  }

  const readMeta = (name) =>
    document
      .querySelector(`meta[name="${name}"]`)
      ?.getAttribute("content")
      ?.trim() ?? "";

  const project =
    readMeta("readthedocs-project-slug") ||
    window.READTHEDOCS_DATA?.project ||
    "";
  const version =
    readMeta("readthedocs-version-slug") ||
    window.READTHEDOCS_DATA?.version ||
    "";

  if (!project || !version) {
    return;
  }

  const endpoint = new URL("/_/api/v3/search/", window.location.origin);
  endpoint.searchParams.set("q", `project:${project}/${version} ${query}`);

  const getResultUrl = (result) => {
    const block = result.blocks?.find((item) => item.type === "section");
    const url = new URL(result.path || "/", result.domain || window.location.origin);

    if (block?.id) {
      url.hash = block.id;
    }

    return url.toString();
  };

  const firstSectionBlock = (result) =>
    result.blocks?.find((item) => item.type === "section") ?? null;

  const renderResults = (payload) => {
    const fragment = document.createDocumentFragment();
    const summary = document.createElement("p");
    const results = payload.results ?? [];
    const count = payload.count ?? results.length;

    summary.className = "rtd-server-search-summary";
    summary.textContent =
      count === 0
        ? `No server-side results for "${query}".`
        : `${count} server-side result${count === 1 ? "" : "s"} for "${query}".`;
    fragment.append(summary);

    for (const result of results) {
      const block = firstSectionBlock(result);
      const article = document.createElement("article");
      const heading = document.createElement("h2");
      const link = document.createElement("a");
      const meta = document.createElement("p");

      article.className = "rtd-server-search-result";
      link.href = getResultUrl(result);
      link.textContent = result.title || result.path || "Search result";
      heading.append(link);
      article.append(heading);

      meta.className = "rtd-server-search-meta";
      meta.textContent = `${result.project?.slug || project} / ${result.version?.slug || version}`;
      article.append(meta);

      if (block?.title && block.title !== result.title) {
        const section = document.createElement("p");
        section.className = "rtd-server-search-section";
        section.textContent = block.title;
        article.append(section);
      }

      if (block?.content) {
        const snippet = document.createElement("p");
        snippet.textContent = block.content;
        article.append(snippet);
      }

      fragment.append(article);
    }

    searchResults.replaceChildren(fragment);
  };

  searchResults.setAttribute("aria-busy", "true");

  fetch(endpoint, {
    headers: {
      Accept: "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Search request failed with status ${response.status}`);
      }

      return response.json();
    })
    .then(renderResults)
    .catch((error) => {
      const message = document.createElement("p");
      message.className = "rtd-server-search-summary";
      message.textContent = `${error.message}. Falling back to the bundled Sphinx search results if they are available.`;

      if (searchResults.firstChild) {
        searchResults.prepend(message);
      } else {
        searchResults.append(message);
      }
    })
    .finally(() => {
      searchResults.removeAttribute("aria-busy");
    });
});
