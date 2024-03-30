const loadUserDetails = () => {
    const user_id = localStorage.getItem("user_id");
    
  fetch(`http://testing-8az5.onrender.com/users/${user_id}`)
    .then((res) => res.json())
    .then((data) => console.log(data));
};

loadUserDetails();
