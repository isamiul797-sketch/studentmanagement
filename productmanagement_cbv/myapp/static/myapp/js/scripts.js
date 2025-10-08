// Define the base API URL 
const API_URL ='api/products/';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const productList =document.getElementById('product-list')
const addProductForm =document.getElementById('add-product-form');

const formTitle = document.getElementById('form-title');

function showFormErrors(errors) {
    document.getElementById('name-error').textContent ='';
    document.getElementById('price-error').textContent ='';
    if (errors.name){
        document.getElementById('name-error').textContent =errors.name[0];
    }
    if (errors.price){
        document.getElementById('price-error').textContent =errors.price[0];
    }
}
 function handleEdit(event){
    const id = event.target.dataset.id
    const name = event.target.dataset.name
    const price = event.target.dataset.price

    document.getElementById('product-id').value = id;
    document.getElementById('name').value = name;
    document.getElementById('price').value = price;

    formTitle.textContent = 'Edit Product';

 }

 function handleView(event){
    const id = event.target.dataset.id
    window.location.href = `/product/${id}/`;
 }

function addButtonsEventListeners(){
    const editButton = document.querySelectorAll('.edit-btn');
    const deleteButton = document.querySelectorAll('.delete-btn');
    const viewButton = document.querySelectorAll('.view-btn');
    editButton.forEach(button => {
        button.addEventListener('click', handleEdit);
    });
    deleteButton.forEach(button => {
        button.addEventListener('click', handleDelete);
    });
    viewButton.forEach(button => {
        button.addEventListener('click', handleView);
    });
}

async function fetchProducts(){
    const response = await fetch(API_URL);
    if(response.ok){
        const products = await  response.json()
        productList.innerHTML = products.map(product =>` <tr>
                <td>${product.id}</td>
                <td>${product.name}</td>
                <td>${product.price}</td>
                <td>
                    <button class='btn btn-sm btn-info view-btn' data-id="${product.id}" >View</button>
                    <button class='btn btn-sm btn-warning edit-btn' data-id="${product.id}" data-name="${product.name}" data-price="${product.price}">Edit</button>
                    <button class='btn btn-sm btn-danger delete-btn' data-id="${product.id}">Delete</button>
                </td>
            </tr>
        `)
        addButtonsEventListeners()
    } else{
        console.error("failed to fetch products")
    }
}
fetchProducts()

addProductForm.addEventListener('submit', async(event)=>{
    event.preventDefault()
    const id = document.getElementById('product-id').value;
    const name = document.getElementById('name').value;
    const price = document.getElementById('price').value;

    const method = id ? 'PUT' : 'POST'
    const url = id ? `${API_URL}${id}/` : API_URL
    const response = await fetch(url,{
        method : method,
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({name,price})
    });
    if (response.ok){
        await fetchProducts();
        addProductForm.reset()
    }else{
        const errorData = await response.json()
        showFormErrors(errorData)
    }
})

async function handleDelete(event){
    const id = event.target.dataset.id
    const response = await fetch(`${API_URL}${id}/`,{
        method : 'DELETE',
        headers:{
            'X-CSRFToken': csrftoken,
        },
    })
    if(response.ok){
        await fetchProducts();
    }else{
        console.error('Failed to delete product')
    }
}