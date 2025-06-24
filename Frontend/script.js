const API_URL = "http://localhost:8000/smart_search";
const DEFAULT_API = "https://fakestoreapi.com/products";

window.onload = () => {
  fetchInitialProducts();
};

async function fetchInitialProducts() {
  const resultsContainer = document.getElementById("resultsContainer");
  resultsContainer.innerHTML = "Loading products...";

  try {
    const response = await fetch(DEFAULT_API);
    const products = await response.json();

    resultsContainer.innerHTML = "";
    products.forEach(product => {
      const card = document.createElement("div");
      card.className = "card";

      card.innerHTML = `
        <img src="${product.image}" alt="${product.title}" />
        <h3>${product.title}</h3>
        <p>${product.description.substring(0, 80)}...</p>
        <p><strong>Price:</strong> $${product.price}</p>
        <p><strong>Rating:</strong> ${product.rating.rate} (${product.rating.count} reviews)</p>
        <p><strong>Category:</strong> ${product.category}</p>
      `;

      resultsContainer.appendChild(card);
    });
  } catch (err) {
    resultsContainer.innerHTML = "<p>Error loading initial products.</p>";
    console.error(err);
  }
}

async function performSearch() {
  const query = document.getElementById("searchInput").value.trim();
  const resultsContainer = document.getElementById("resultsContainer");

  if (!query) {
    fetchInitialProducts();  // fallback to default
    return;
  }

  resultsContainer.innerHTML = "Searching...";

  try {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    });

    const data = await response.json();

    if (!data.results || data.results.length === 0) {
      resultsContainer.innerHTML = "<p>No matching products found.</p>";
      return;
    }

    resultsContainer.innerHTML = "";
    data.results.forEach(product => {
      const card = document.createElement("div");
      card.className = "card";

      card.innerHTML = `
        <img src="${product.metadata.image_url}" alt="${product.metadata.product_id}" />
        <h3>${product.content.split(":")[0]}</h3>
        <p>${product.content.split(":")[1]}</p>
        <p><strong>Price:</strong> $${product.metadata.price}</p>
        <p><strong>Rating:</strong> ${product.metadata.rating_score} (${product.metadata.rating_count} reviews)</p>
        <p><strong>Category:</strong> ${product.metadata.category}</p>
      `;

      resultsContainer.appendChild(card);
    });

  } catch (err) {
    resultsContainer.innerHTML = "<p>Error fetching smart results.</p>";
    console.error(err);
  }
}
