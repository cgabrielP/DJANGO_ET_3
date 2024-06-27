const addToCart = (productId, productName, productPrice, productImage) => {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  let product = cart.find(item => item.id === productId);
  console.log(productId);
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
  alert('Producto agregado al carrito');
};

window.addToCart = addToCart;


const removeFromCart=(productId)=>{
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  let product = cart.find(item => item.id === productId);
  localStorage.removeItem()
  //por terminar
}

