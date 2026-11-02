import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa đầu tiên
        for i in range(20):
            dvd = DigitalVideoDisc(f"Movie {i}", "Category", 10.0)
            self.assertTrue(cart.add_dvd(dvd)) # Sửa add_cart thành add_dvd
            
        # Thử thêm đĩa thứ 21 -> Lẽ ra phải trả về False vì vượt quá giới hạn
        extra_dvd = DigitalVideoDisc("Movie Extra", "Category", 10.0)
        self.assertFalse(cart.add_dvd(extra_dvd), "Giỏ hàng không được phép nhận quá 20 đĩa!") # Sửa add_cart thành add_dvd

if __name__ == '__main__':
    unittest.main()