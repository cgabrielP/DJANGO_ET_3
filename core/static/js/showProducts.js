window.onload = function () {
    renderOrder();
  };
  
const renderOrder = () => {
    let products = JSON.parse(localStorage.getItem('cart')) || [];
    const productsContainer = document.getElementById('orderProducts');
    productsContainer.innerHTML = '';
  
    products.forEach(item => {
      const orderItem = document.createElement('div');
      orderItem.className = 'row border-bottom';
  
      orderItem.innerHTML = `
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
  
      productsContainer.appendChild(orderItem);
    });
  

  };