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

  const escapeHtml = (value) =>
    (value ?? "").replace(/[&<>"']/g, (char) => {
      const entities = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;",
      };

      return entities[char];
    });

  const truncateText = (value, maxLength = 220) => {
    const text = (value ?? "").replace(/\s+/g, " ").trim();

    if (text.length <= maxLength) {
      return text;
    }

    return `${text.slice(0, maxLength - 1).trimEnd()}…`;
  };

  const sectionBlocks = (result) => {
    const blocks = result.blocks?.filter((item) => item.type === "section") ?? [];

    return blocks.length > 0 ? blocks : [null];
  };

  const resultUrl = (result, block) => {
    const url = new URL(result.path || "/", result.domain || window.location.origin);

    if (block?.id) {
      url.hash = block.id;
    }

    return url.toString();
  };

  const pageTitleHtml = (result) =>
    result.highlights?.title?.[0] ||
    escapeHtml(result.title || result.path || "Search result");

  const blockTitleHtml = (block) =>
    block?.highlights?.title?.[0] ||
    (block?.title ? escapeHtml(block.title) : "");

  const resultTitleHtml = (result, block) => {
    const pageTitle = pageTitleHtml(result);
    const blockTitle = blockTitleHtml(block);

    if (blockTitle && block?.title !== result.title) {
      return `${pageTitle} <span class="rtd-server-search-separator">&rsaquo;</span> ${blockTitle}`;
    }

    return blockTitle || pageTitle;
  };

  const snippetHtml = (block) => {
    const highlighted = block?.highlights?.content?.[0];

    if (highlighted) {
      return highlighted;
    }

    if (!block?.content) {
      return "";
    }

    return escapeHtml(truncateText(block.content));
  };

  const renderResults = (payload) => {
    const results = payload.results ?? [];

    if (results.length === 0) {
      return false;
    }

    const title = document.createElement("h2");
    const summary = document.createElement("p");
    const list = document.createElement("ul");

    title.textContent = "Search Results";

    summary.className = "search-summary rtd-server-search-summary";
    summary.textContent = `Found ${payload.count ?? results.length} server-side result${
      (payload.count ?? results.length) === 1 ? "" : "s"
    } for "${query}".`;

    list.className = "search rtd-server-search-list";

    for (const result of results) {
      for (const block of sectionBlocks(result)) {
        const item = document.createElement("li");
        const link = document.createElement("a");
        const context = document.createElement("span");
        const snippet = snippetHtml(block);

        link.href = resultUrl(result, block);
        link.innerHTML = resultTitleHtml(result, block);
        item.append(link);

        context.className = "rtd-server-search-context";
        context.textContent = ` (${(result.path || "").replace(/^\//, "")})`;
        item.append(context);

        if (snippet) {
          const snippetNode = document.createElement("p");
          snippetNode.className = "rtd-server-search-snippet";
          snippetNode.innerHTML = snippet;
          item.append(snippetNode);
        }

        list.append(item);
      }
    }

    searchResults.replaceChildren(title, summary, list);
    return true;
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
    .then((payload) => {
      renderResults(payload);
    })
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
