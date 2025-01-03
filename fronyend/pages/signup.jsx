import { useState } from "react";
import { signup } from "../src/api";

const Signup = () => {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [error, setError] = useState("");
    const [success, setSuccess] = useState(false);
    const [loading, setLoading] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
};

const handlechange = (e) => {
    const { name, value } = e.target;
    switch (name) {
        case "username":
            setUsername(value);
            break;
            case "email":
                setEmail(value);
                break;
                case "password":
                    setPassword(value);

}

const handleSubmit = async (e) => {
    e.preventDefault();
try{
    await signup(formdata);
  alert("Signup successful! Please Login")
}catch(error){
    alert("Signup Failed")
}
};

return{
    <form onSubmit={handleSubmit} className = "signup">
    <h1 className="text -2*1 font-bold mb-4">Signup
    <input
    type="text"
    name="username"
    value={username}
    placeholder="Username"
    onChange={handlechange}
    className="signup"
    />
    <input
    type="email"
    name="email"
    placeholder={email}
    onChange={handlechange}
    className="signup"
    />
    <input
    type="password"
    name="password"
    placeholder="password"
    onChange={handlechange}
    className="signup"
    />

    <button type="submit" className="bg-blue-600 text-white p-2 w-full">
    Signup
  </button>
</form>

};

export default Signup;