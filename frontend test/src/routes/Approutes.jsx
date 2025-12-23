import { Route,Routes } from "react-router-dom"
import First from "../pages/First"
import About from "../pages/About"
import Features from "../pages/Features"
import Contact from "../pages/Contact"
import BuyerSignup from "../pages/Buyersignup"
import BuyerLogin from "../pages/BuyerLogin"
import SellerSignup from "../pages/Sellersignup"
import SellerLogin from "../pages/Loginasseller" 

function Approutes() {
  return (
    <>
    <Routes>
      <Route path="/"  element={<First></First>} />
      <Route path="/about" element={<About></About>} />
      <Route path="/features" element={<Features></Features>} />
      <Route path="/contact" element={<Contact></Contact>} />
      <Route path="/Buyersignup" element={<BuyerSignup></BuyerSignup>} />
      <Route path="/BuyerLogin" element={<BuyerLogin></BuyerLogin>} />
      <Route path="/Sellersignup" element={<SellerSignup></SellerSignup>} />
      <Route path="/Loginasseller" element={<SellerLogin></SellerLogin>} />
    </Routes>
    </>
  )
}

export default Approutes