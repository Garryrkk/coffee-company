import react from "react";

const profile = ({user}) => {
    return (
        <div className="profile">
            <h1>Profile</h1>
            <p><strong>Username:</strong>{user.username}</p>
            <p><strong>Email:</strong>{user.email}</p>
            <p><strong>Joined On:</strong>{user.joinDate}</p>
        </div>
    );
};

export default Profile;