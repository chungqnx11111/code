const apiUrl = "https://dummyjson.com/products";
let products = [];
let filteredProducts = [];
let categories = [];
let currentPage = 1;
const itemsPerPage = 6;

// Fetch dữ liệu từ API
fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        products = data.products;
        filteredProducts = [...products];

        // Lấy danh mục sản phẩm duy nhất
        categories = [...new Set(products.map(p => p.category))];
        renderCategories();
        renderProducts();
    });

// Hiển thị danh mục sản phẩm
function renderCategories() {
    const categoryContainer = document.getElementById("category-container");
    categoryContainer.innerHTML = `<button class="category-btn" onclick="filterByCategory('')">Tất cả</button>`;
    
    categories.forEach(category => {
        categoryContainer.innerHTML += `<button class="category-btn" onclick="filterByCategory('${category}')">${category}</button>`;
    });
}

// Lọc sản phẩm theo danh mục
function filterByCategory(category) {
    if (category) {
        filteredProducts = products.filter(p => p.category === category);
    } else {
        filteredProducts = [...products];
    }
    currentPage = 1;
    renderProducts();
}

// Tìm kiếm, sắp xếp sản phẩm
function filterProducts() {
    const searchTerm = document.getElementById("search").value.toLowerCase();
    const sortValue = document.getElementById("sort").value;

    filteredProducts = products.filter(p => p.title.toLowerCase().includes(searchTerm));

    if (sortValue === "priceLowHigh") {
        filteredProducts.sort((a, b) => a.price - b.price);
    } else if (sortValue === "priceHighLow") {
        filteredProducts.sort((a, b) => b.price - a.price);
    } else if (sortValue === "discount") {
        filteredProducts.sort((a, b) => b.discountPercentage - a.discountPercentage);
    }

    currentPage = 1;
    renderProducts();
}

// Phân trang sản phẩm
function changePage(step) {
    const totalPages = Math.ceil(filteredProducts.length / itemsPerPage);
    currentPage = Math.max(1, Math.min(currentPage + step, totalPages));
    renderProducts();
}

// Hiển thị danh sách sản phẩm
function renderProducts() {
    const productList = document.getElementById("product-list");
    const pageInfo = document.getElementById("page-info");

    const totalPages = Math.ceil(filteredProducts.length / itemsPerPage);
    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;

    const displayedProducts = filteredProducts.slice(start, end);

    productList.innerHTML = displayedProducts.map(product => `
        <div class="product-card">
            <img src="${product.thumbnail}" alt="${product.title}">
            <h3>${product.title}</h3>
            <p>Giá: $${product.price}</p>
            <p style="color: red;">-${product.discountPercentage}%</p>
        </div>
    `).join("");

    pageInfo.innerText = `Trang ${currentPage} / ${totalPages}`;
}
