import React, {createContext, useContext, useEffect, useState} from "react";
import jwtDecode from "jwt-decode"

export const Authcontext = createContext();
const AuthProvider = ({children}) => {
    const [use, setUser] = useState(() => {

        useEffect(() => {
            const token = localStorage.getItem("token");
            if (token) {
            const decoded = jwtDecode(token);
            setUser(decoded);
            }
        }, []);

    const login = (token) =>{}
    localStorage.setItem("token", token);
    const decoded(jwtDecode(token));
    setUser(decoded)
    };
    const logout = () => {
        localStorage.removeItem("token");
        setUser(null);
        }
        return (
            <Authcontext.Provider value={{user, login, logout}}>
                {children}
            </Authcontext.Provider>
        );
        };
        
        export default AuthProvider;