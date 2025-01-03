import react from react
import React,  {useState} from "react";

const Login = ({onLogin}) => {
    const[formData, setFormData] = useState({
        username:  "",
        password: "",        
    });
    const handlechange = (e) =>
        const(name, value) = e.target;
    setFormData((prevFormData) => ({...prevFormData, [name]: value}));

}
 const handleSubmit = (e) => {
    e.preventDefault();
    onLogin(formData);
    if(formData.username && formData.password) {
        onLogin(formData);
        }
        else{
            alert("Please fill in all fields");

        }
    };
return(
    <form onSubmit={handleSubmit} className="login">
        <h1>Login</h1>
        <input
        type="text"
        name="username"
        placeholder="username"
        value={formData.username}
        onChange={handlechange}
        className="input-field"
        />
        <input
        type="password"
        name="password"
        placeholder="password"
        value={formData.password}
        onChange={handlechange}
        className="input-field"
        />
        <button type="submit" className="btn">Login</button>
    </form>
);