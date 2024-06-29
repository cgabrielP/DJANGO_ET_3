window.onload = function () {
  renderCart();
};

const addToCart = (productId, productName, productPrice, productImage) => {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  let product = cart.find(item => item.id === productId);

  if (product) {
    product.quantity += 1;
  } else {
    cart.push({
      id: productId,
      name: productName,
      price: productPrice,
      image: productImage,
      quantity: 1
    });
  }

  localStorage.setItem('cart', JSON.stringify(cart));
  renderCart();
};
const cartLength=()=>{
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  let amountOfProducts=document.getElementById('cart-length')
  amountOfProducts.innerHTML=cart.length;
}

const renderCart = () => {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  console.log(cart);
  const cartContainer = document.getElementById('cart-container');
  cartContainer.innerHTML = '';

  cart.forEach(item => {
    const cartItem = document.createElement('div');
    cartItem.className = 'row border-bottom';

    cartItem.innerHTML = `
      <div class="col-9">
        <div class="mb-3">
          <div class="row g-0">
            <div class="col-md-5">
              <img src="${item.image}" class="img-fluid rounded-start" alt="${item.name}" />
            </div>
            <div class="col-md-7">
              <div class="card-body ms-1">
                <div class="card-title fs-6">${item.name}</div>
                <div class="btn-group align-items-center mt-2" role="group" aria-label="Basic example">
                  <button type="button" class="btn btn-success" onclick="removeFromCart(${item.id})">
                    <i class="fa-solid fa-trash-can"></i>
                  </button>
                  <div class="px-1">${item.quantity} un.</div>
                  <button type="button" class="btn btn-success" onclick="increaseQuantity(${item.id})">
                    <i class="fa-solid fa-plus"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-3">
        <div class="fw-bold">$${item.price}</div>
        <div role="button" class="fw-bold mt-5 text-success text-decoration-underline" onclick="removeFromCart(${item.id})">
          Eliminar
        </div>
      </div>
    `;

    cartContainer.appendChild(cartItem);
  });

  updateCartSummary(cart);
  cartLength();
};

const removeFromCart = (productId) => {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  let index = cart.findIndex((item) => {
    return parseInt(item.id) === productId;
  });

  if (index !== -1) {
    cart.splice(index, 1);

    localStorage.setItem('cart', JSON.stringify(cart));
  }
  renderCart();
};

const increaseQuantity = (productId) => {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  let index = cart.findIndex((item) => parseInt(item.id) === productId);
  cart[index].quantity++;
  localStorage.setItem('cart', JSON.stringify(cart));
  renderCart();
  
};

const updateCartSummary = (cart) => {
  const total = calculateTotal(cart);
  const subtotalElement = document.getElementById('subtotal');
  const buyButton = document.getElementById('buy-button');

  if (subtotalElement) {
    subtotalElement.textContent = `$${total}`;
  }


  if (total < 10000) {
    buyButton.setAttribute('disabled', true);
    buyButton.classList.add('btn-secondary')
    buyButton.classList.remove('btn-success')
  } else {
    buyButton.removeAttribute('disabled',);
    buyButton.classList.add('btn-success')
    buyButton.classList.remove('btn-secondary')
  }

};

const calculateTotal = (cart) => {
  return cart.reduce((total, item) => total + item.price * item.quantity, 0);
};
