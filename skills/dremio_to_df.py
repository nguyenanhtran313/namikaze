"""
Bí kíp: Truy vấn dữ liệu từ Dremio ra Pandas DataFrame.
Người thực hiện: Antigravity (Bé DA 26 tuổi)
"""

import pandas as pd
from pyarrow import flight

def get_dremio_dataframe(query, host, port=32010, username=None, password=None):
    """
    Kết nối Dremio qua Arrow Flight và trả về DataFrame.
    """
    try:
        # 1. Khởi tạo Flight Client
        location = f"grpc+tcp://{host}:{port}"
        client = flight.FlightClient(location)
        
        # 2. Xác thực (Authentication)
        bearer_token = client.authenticate_basic_token(username, password)
        options = flight.FlightCallOptions(headers=[bearer_token])

        # 3. Gửi truy vấn
        descriptor = flight.FlightDescriptor.for_command(query)
        info = client.get_flight_info(descriptor, options)
        
        # 4. Lấy dữ liệu và chuyển đổi
        reader = client.do_get(info.endpoints[0].ticket, options)
        table = reader.read_all()
        df = table.to_pandas()
        
        print(f"✅ Đã lấy thành công {len(df)} dòng dữ liệu từ Dremio.")
        return df
        
    except Exception as e:
        print(f"❌ Lỗi kết nối Dremio rồi anh ơi: {e}")
        return None

if __name__ == "__main__":
    # Ví dụ mẫu để anh chạy thử:
    # SQL = 'SELECT * FROM "Space"."Folder"."Table"'
    # my_df = get_dremio_dataframe(SQL, "localhost", username="user", password="pass")
    pass
