/* Awesome DSH Plugins — landing page app
   Vanilla JS, no dependencies. Data: ./data/meta.json + per-category shards. */
(function () {
  "use strict";

  var PAGE_SIZE = 48;

  /* ---------- i18n ---------- */

  var I18N = {
    zh: {
      heroBadge: "社区目录 · 每 8 小时自动同步",
      heroTitle: '一切皆<span class="grad">插件</span>',
      heroSub: '发现并搜索 DeepSeek Harness 生态中的社区插件，全部收录自 GitHub topic <code>dsh-plugin</code>。',
      searchPlaceholder: "搜索插件、功能、话题…",
      statTotal: "插件", statCats: "分类", statUpdated: "最近同步",
      all: "全部", sortLabel: "排序",
      sortStars: "最多 Star", sortUpdated: "最近更新", sortName: "名称",
      resultInfo: function (n) { return "共 <b>" + fmt(n) + "</b> 个插件"; },
      emptyTitle: "没有找到匹配的插件",
      emptySub: "换个关键词试试，或清除筛选条件",
      clearBtn: "清除筛选",
      loadingMore: "加载中…",
      footerDesc: "DeepSeek Harness 社区插件精选，由 GitHub topic dsh-plugin 自动收录与分类。",
      footerRepo: "GitHub 仓库", footerHarness: "DeepSeek Harness", footerContrib: "参与收录",
      footerMeta: "数据每 8 小时自动同步 · CC0 1.0",
      footerAffil: "与 DeepSeek 官方无关的社区项目",
      langBtn: "EN", htmlLang: "zh-CN",
      dateLocale: "zh-CN",
    },
    en: {
      heroBadge: "Community Directory · Auto-synced every 8h",
      heroTitle: 'Everything is a <span class="grad">Plugin</span>',
      heroSub: 'Discover and search community plugins for the DeepSeek Harness ecosystem, collected from the GitHub topic <code>dsh-plugin</code>.',
      searchPlaceholder: "Search plugins, features, topics…",
      statTotal: "Plugins", statCats: "Categories", statUpdated: "Last sync",
      all: "All", sortLabel: "Sort",
      sortStars: "Most stars", sortUpdated: "Recently updated", sortName: "Name",
      resultInfo: function (n) { return "<b>" + fmt(n) + "</b> plugins"; },
      emptyTitle: "No plugins found",
      emptySub: "Try a different keyword or clear the filters",
      clearBtn: "Clear filters",
      loadingMore: "Loading…",
      footerDesc: "A curated directory of DeepSeek Harness community plugins, auto-collected and categorized from the GitHub topic dsh-plugin.",
      footerRepo: "GitHub Repo", footerHarness: "DeepSeek Harness", footerContrib: "Contribute",
      footerMeta: "Auto-synced every 8 hours · CC0 1.0",
      footerAffil: "Community project, not affiliated with DeepSeek",
      langBtn: "中", htmlLang: "en",
      dateLocale: "en-US",
    },
  };

  /* ---------- state ---------- */

  var state = {
    lang: localStorage.getItem("dsh-lang") || "zh",
    theme: localStorage.getItem("dsh-theme") || "dark",
    cat: "all",
    q: "",
    sort: "stars",
    visible: PAGE_SIZE,
    plugins: [],      // all loaded plugins, each with ._cat
    meta: null,
  };

  /* ---------- dom ---------- */

  var $ = function (id) { return document.getElementById(id); };
  var els = {
    chips: $("chips"), grid: $("grid"), empty: $("empty"), sentinel: $("sentinel"),
    resultInfo: $("resultInfo"), searchInput: $("searchInput"), sortSelect: $("sortSelect"),
    statTotal: $("statTotal"), statCats: $("statCats"), statUpdated: $("statUpdated"),
  };

  /* ---------- utils ---------- */

  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ","); }

  function fmtStars(n) {
    if (n >= 1000) return (n / 1000).toFixed(n >= 10000 ? 0 : 1).replace(/\.0$/, "") + "k";
    return String(n);
  }

  function esc(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function escRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }

  var STAR_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2l2.9 6.26 6.85.72-5.1 4.6 1.43 6.72L12 16.9l-6.08 3.4 1.43-6.72-5.1-4.6 6.85-.72z"/></svg>';
  var ARROW_SVG = '<svg class="card-arrow" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></svg>';

  /* ---------- i18n apply ---------- */

  function t() { return I18N[state.lang]; }

  function applyI18n() {
    var L = t();
    document.documentElement.lang = L.htmlLang;
    $("heroBadge").textContent = L.heroBadge;
    $("heroTitle").innerHTML = L.heroTitle;
    $("heroSub").innerHTML = L.heroSub;
    els.searchInput.placeholder = L.searchPlaceholder;
    $("statTotalLabel").textContent = L.statTotal;
    $("statCatsLabel").textContent = L.statCats;
    $("statUpdatedLabel").textContent = L.statUpdated;
    $("sortLabel").textContent = L.sortLabel;
    $("optStars").textContent = L.sortStars;
    $("optUpdated").textContent = L.sortUpdated;
    $("optName").textContent = L.sortName;
    $("emptyTitle").textContent = L.emptyTitle;
    $("emptySub").textContent = L.emptySub;
    $("clearBtn").textContent = L.clearBtn;
    $("footerDesc").textContent = L.footerDesc;
    $("footerRepo").textContent = L.footerRepo;
    $("footerHarness").textContent = L.footerHarness;
    $("footerContrib").textContent = L.footerContrib;
    $("footerMeta").textContent = L.footerMeta;
    $("footerAffil").textContent = L.footerAffil;
    $("langToggle").textContent = L.langBtn;
  }

  /* ---------- data loading ---------- */

  function loadData() {
    return fetch("data/meta.json").then(function (r) { return r.json(); }).then(function (meta) {
      state.meta = meta;
      var files = meta.categories.map(function (c) {
        return fetch("data/" + c.slug + ".json")
          .then(function (r) { return r.json(); })
          .then(function (items) {
            items.forEach(function (it) { it._cat = c.slug; });
            return items;
          });
      });
      return Promise.all(files).then(function (groups) {
        state.plugins = [].concat.apply([], groups);
        renderMeta();
        renderChips();
        apply();
      });
    });
  }

  function renderMeta() {
    els.statTotal.textContent = fmt(state.meta.total);
    els.statCats.textContent = String(state.meta.categories.length);
    els.statUpdated.textContent = state.meta.generated_at || "—";
  }

  /* ---------- chips ---------- */

  function renderChips() {
    var L = t();
    var html = chipHtml("all", "🧩", L.all, state.meta.total, state.cat === "all");
    state.meta.categories.forEach(function (c) {
      html += chipHtml(c.slug, c.icon, state.lang === "zh" ? c.zh : c.en, c.count, state.cat === c.slug);
    });
    els.chips.innerHTML = html;
    Array.prototype.forEach.call(els.chips.querySelectorAll(".chip"), function (el) {
      el.addEventListener("click", function () {
        state.cat = el.getAttribute("data-cat");
        state.visible = PAGE_SIZE;
        renderChips();
        apply();
      });
    });
  }

  function chipHtml(slug, icon, label, count, active) {
    return '<button class="chip' + (active ? " active" : "") + '" data-cat="' + slug + '" role="tab" aria-selected="' + active + '">'
      + '<span>' + icon + "</span><span>" + esc(label) + '</span><span class="chip-count">' + fmt(count) + "</span></button>";
  }

  /* ---------- search + filter + sort ---------- */

  function score(p, tokens) {
    var name = p.full_name.toLowerCase();
    var desc = (p.description || "").toLowerCase();
    var topics = (p.topics || []).join(" ").toLowerCase();
    var total = 0;
    for (var i = 0; i < tokens.length; i++) {
      var tk = tokens[i], s = 0;
      if (name.indexOf(tk) !== -1) s += 30;
      if (topics.indexOf(tk) !== -1) s += 10;
      if (desc.indexOf(tk) !== -1) s += 4;
      if (s === 0) return -1; // AND semantics
      total += s;
    }
    return total;
  }

  function currentList() {
    var list = state.plugins;
    if (state.cat !== "all") {
      list = list.filter(function (p) { return p._cat === state.cat; });
    }
    var tokens = state.q.trim().toLowerCase().split(/\s+/).filter(Boolean);
    if (tokens.length) {
      var scored = [];
      for (var i = 0; i < list.length; i++) {
        var s = score(list[i], tokens);
        if (s > 0) { list[i]._score = s; scored.push(list[i]); }
      }
      list = scored;
    }
    var sorters = {
      stars: function (a, b) { return (b._score || 0) - (a._score || 0) || b.stars - a.stars || a.full_name.localeCompare(b.full_name); },
      updated: function (a, b) { return (b.updated_at || "").localeCompare(a.updated_at || "") || b.stars - a.stars; },
      name: function (a, b) { return a.full_name.localeCompare(b.full_name); },
    };
    return list.slice().sort(sorters[state.sort]);
  }

  /* ---------- render ---------- */

  function highlight(text, tokens) {
    if (!tokens.length || !text) return esc(text);
    var re = new RegExp("(" + tokens.map(escRe).join("|") + ")", "gi");
    return esc(text).replace(re, "<mark>$1</mark>");
  }

  function cardHtml(p, tokens) {
    var parts = p.full_name.split("/");
    var owner = parts.length > 1 ? parts.slice(0, -1).join("/") : "";
    var repo = parts.length > 1 ? parts[parts.length - 1] : p.full_name;
    var topics = (p.topics || []).slice(0, 4);
    var extra = (p.topics || []).length - topics.length;
    var topicsHtml = topics.map(function (tp) {
      return '<span class="topic">' + highlight(tp, tokens) + "</span>";
    }).join("");
    if (extra > 0) topicsHtml += '<span class="topic more">+' + extra + "</span>";
    var date = p.updated_at ? p.updated_at.slice(0, 10) : "";
    return '<a class="card" href="' + esc(p.url) + '" target="_blank" rel="noopener">'
      + '<div class="card-top"><span class="card-name">'
      + (owner ? '<span class="owner">' + esc(owner) + '/</span>' : "")
      + highlight(repo, tokens) + "</span>"
      + '<span class="card-stars">' + STAR_SVG + fmtStars(p.stars) + "</span></div>"
      + '<p class="card-desc">' + highlight(p.description || "", tokens) + "</p>"
      + (topicsHtml ? '<div class="card-topics">' + topicsHtml + "</div>" : "")
      + '<div class="card-foot"><span class="card-date">' + date + "</span>" + ARROW_SVG + "</div></a>";
  }

  function apply() {
    var L = t();
    var tokens = state.q.trim().toLowerCase().split(/\s+/).filter(Boolean);
    var list = currentList();
    var shown = list.slice(0, state.visible);

    var html = "";
    for (var i = 0; i < shown.length; i++) html += cardHtml(shown[i], tokens);
    if (list.length > state.visible) {
      html += '<div class="loading-more" id="loadingMore">' + L.loadingMore + "</div>";
    }
    els.grid.innerHTML = html;
    els.empty.hidden = list.length > 0;
    els.resultInfo.innerHTML = L.resultInfo(list.length);

    if (list.length > state.visible) setupInfiniteScroll(list);
  }

  var observer = null;
  function setupInfiniteScroll(list) {
    if (observer) observer.disconnect();
    observer = new IntersectionObserver(function (entries) {
      if (entries[0].isIntersecting && state.visible < list.length) {
        state.visible += PAGE_SIZE;
        apply();
      }
    }, { rootMargin: "600px 0px" });
    observer.observe(els.sentinel);
  }

  /* ---------- url params ---------- */

  function readUrl() {
    var sp = new URLSearchParams(location.search);
    if (sp.get("lang") === "en") state.lang = "en";
    if (sp.get("lang") === "zh") state.lang = "zh";
    if (sp.get("q")) state.q = sp.get("q");
    if (sp.get("cat")) state.cat = sp.get("cat");
  }

  function writeUrl() {
    var sp = new URLSearchParams();
    if (state.q) sp.set("q", state.q);
    if (state.cat !== "all") sp.set("cat", state.cat);
    if (state.lang !== "zh") sp.set("lang", state.lang);
    var qs = sp.toString();
    history.replaceState(null, "", qs ? "?" + qs : location.pathname);
  }

  /* ---------- events ---------- */

  var debounceTimer = null;
  els.searchInput.addEventListener("input", function () {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function () {
      state.q = els.searchInput.value;
      state.visible = PAGE_SIZE;
      writeUrl();
      apply();
    }, 120);
  });

  els.sortSelect.addEventListener("change", function () {
    state.sort = els.sortSelect.value;
    state.visible = PAGE_SIZE;
    apply();
  });

  $("clearBtn").addEventListener("click", function () {
    state.q = "";
    els.searchInput.value = "";
    state.cat = "all";
    state.visible = PAGE_SIZE;
    renderChips();
    writeUrl();
    apply();
    els.searchInput.focus();
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== els.searchInput) {
      e.preventDefault();
      els.searchInput.focus();
    }
  });

  $("langToggle").addEventListener("click", function () {
    state.lang = state.lang === "zh" ? "en" : "zh";
    localStorage.setItem("dsh-lang", state.lang);
    applyI18n();
    renderChips();
    apply();
    writeUrl();
  });

  $("themeToggle").addEventListener("click", function () {
    state.theme = state.theme === "dark" ? "light" : "dark";
    localStorage.setItem("dsh-theme", state.theme);
    document.documentElement.setAttribute("data-theme", state.theme);
  });

  /* ---------- boot ---------- */

  document.documentElement.setAttribute("data-theme", state.theme);
  readUrl();
  applyI18n();
  els.searchInput.value = state.q;
  loadData().catch(function (err) {
    console.error(err);
    els.resultInfo.textContent = "Failed to load data — /data/meta.json missing?";
  });
})();
