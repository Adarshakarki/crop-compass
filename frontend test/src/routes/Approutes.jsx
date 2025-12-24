import { Route, Routes } from "react-router-dom"
import First from "../pages/First"
import About from "../pages/About"
import Features from "../pages/Features"
import Contact from "../pages/Contact"
import BuyerSignup from "../pages/Buyersignup"
import BuyerLogin from "../pages/BuyerLogin"
import SellerSignup from "../pages/Sellersignup"
import SellerLogin from "../pages/Loginasseller" 
import Success from "../Payment/Success"
import Failure from "../Payment/Failure"
import Payment from "../Payment/Payment"

function Approutes() {
  return (
    <Routes>
      {/* Landing & Info */}
      <Route path="/" element={<First />} />
      <Route path="/about" element={<About />} />
      <Route path="/features" element={<Features />} />
      <Route path="/contact" element={<Contact />} />

      {/* Buyer Authentication */}
      <Route path="/buyersignup" element={<BuyerSignup />} />
      <Route path="/buyerlogin" element={<BuyerLogin />} />

      {/* Seller Authentication */}
      <Route path="/sellersignup" element={<SellerSignup />} />
      <Route path="/loginasseller" element={<SellerLogin />} />

      {/* Payment Status */}
      <Route path="/success" element={<Success />} />
      <Route path="/failure" element={<Failure />} />
      <Route path="/payment" element={<Payment />} />
    </Routes>
  )
}

export default Approutes