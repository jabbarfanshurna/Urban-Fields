import { Link } from "react-router-dom";
import LandingPageButton from "../Elements/Button/LandingPageButton";

const NavBar = () => {
    // Pastikan nama 'token' ini sama dengan yang kamu set di LoginPage saat sukses login
    const isAuthenticated = localStorage.getItem('token');

    return (
        <nav className="flex w-screen top-0 z-20 py-2 px-24 justify-between select-none bg-white shadow-lg sticky">
            <Link to="/" className="flex items-center cursor-pointer">
                <img src="/img/icon.png" alt="logo"/>
                <h1 className="text-black text-2xl font-KronaOne ml-4">URBAN FIELDS</h1>
            </Link>

            <div className="flex items-center text-black text-lg font-Inter ml-52 font-bold">
                {/* Sekarang sudah bisa diklik dan mengarah ke halaman yang benar */}
                <Link to="/fields" className="mx-14 cursor-pointer hover:text-green-600 transition">Our Fields</Link>
                <Link to="/dashboard/orders" className="mx-14 cursor-pointer hover:text-green-600 transition">Reservations</Link>
                <Link to="/" className="mx-14 cursor-pointer hover:text-green-600 transition">About Us</Link>
            </div>

            <div className="flex items-center text-black text-lg font-Inter">
                {isAuthenticated ? (
                    /* Gunakan Link, jangan tag <a> biasa supaya tidak refresh halaman */
                    <Link to="/dashboard" className="mr-20 cursor-pointer">
                        <LandingPageButton textsize='lg'>My Dashboard</LandingPageButton>
                    </Link>
                ) : (
                    <>
                        <Link to="/login" className="mr-20 cursor-pointer hover:text-green-600 transition">Sign In</Link>
                        <Link to="/register" className="cursor-pointer">
                            <LandingPageButton textsize='lg'>Sign Up</LandingPageButton>
                        </Link>
                    </>
                )}
            </div>
        </nav>
    );
}

export default NavBar;