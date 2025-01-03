import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="Container mx-auto flex justify between">
        <Link to="/" className="text-xl font-bold">
        MyApp
        </Link>
        <div>
        <Link to="/signup" className="mx-2 hover:underline">
            Signup
        </Link>
        <Link to="/login" className="mx-2 hover:underline">
            Login
        </Link>
        <Link to="/profile" className="mx-2 hover:underline">
            Profile
        </Link>
        </div>
    </div>
    </nav>
);
};
export default Navbar;
