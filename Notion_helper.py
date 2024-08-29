import constants
import requests
import json

headers = {
    "Authorization": f"Bearer {constants.NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


def log(time: str, content: str):
    # Sử dụng theo dạng append
    txt = f"{time}: {content}"
    data = {
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": txt,
                            },
                            "plain_text": txt,
                        }
                    ],
                }
            }
        ]
    }
    url = f"https://api.notion.com/v1/blocks/{constants.LOG_BLOCK_ID}/children"
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    
    send_notification()
    return response

class Board:

    @staticmethod
    def update_gia_hien_tai(gia_hien_tai: float, block_id: str):
        gia_hien_tai = f"{gia_hien_tai:.3f} VND"
        data = {
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Gi\u00e1 hi\u1ec7n t\u1ea1i: ",
                            "link": None,
                        },
                        "annotations": {
                            "bold": True,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default",
                        },
                        "plain_text": "Gi\u00e1 hi\u1ec7n t\u1ea1i: ",
                        "href": None,
                    },
                    {
                        "type": "text",
                        "text": {"content": gia_hien_tai, "link": None},
                        "annotations": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default",
                        },
                        "plain_text": gia_hien_tai,
                        "href": None,
                    },
                ],
            },
        }
        url = f"https://api.notion.com/v1/blocks/{block_id}"
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        print(response)

        return response

    @staticmethod
    def update_ngay_cap_nhat_gan_nhat(ngay_cap_nhat_gan_nhat: str, block_id: str):
        data = {
            "paragraph": {
                "rich_text": [
                    {
                        "text": {"content": ngay_cap_nhat_gan_nhat},
                        "plain_text": ngay_cap_nhat_gan_nhat,
                    }
                ],
            },
        }
        url = f"https://api.notion.com/v1/blocks/{block_id}"
        response = requests.patch(url, headers=headers, data=json.dumps(data))

        return response

    @staticmethod
    def update_so_ngay_cap_nhat_gan_nhat(so_ngay_cap_nhat_gan_nhat: int, block_id: str):
        content = f"{so_ngay_cap_nhat_gan_nhat} Ngày"
        data = {
            "paragraph": {
                "rich_text": [
                    {
                        "text": {"content": content},
                        "plain_text": content,
                    }
                ],
            },
        }
        url = f"https://api.notion.com/v1/blocks/{block_id}"
        response = requests.patch(url, headers=headers, data=json.dumps(data))

        return response

    @staticmethod
    def update_tinh_trang(tinh_trang: str, block_id: str):
        data = {
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "Tình trạng: "},
                        "annotations": {
                            "bold": True,
                        },
                        "plain_text": "Tình trạng: ",
                    },
                    {
                        "type": "text",
                        "text": {"content": tinh_trang},
                        "annotations": {
                            "bold": True,
                            "color": "green" if tinh_trang.lower() == "giảm" else "red",
                        },
                        "plain_text": tinh_trang,
                    },
                ],
            },
        }
        url = f"https://api.notion.com/v1/blocks/{block_id}"
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        print(response)
        return response


class XANG_RON_95_III(Board):

    @staticmethod
    def update_gia_hien_tai(gia_hien_tai: float):
        Board.update_gia_hien_tai(
            gia_hien_tai, constants.XANG_RON_95_III.GIA_HIEN_TAI_BLOCK_ID
        )

    @staticmethod
    def update_ngay_cap_nhat_gan_nhat(ngay_cap_nhat_gan_nhat: str):
        Board.update_ngay_cap_nhat_gan_nhat(
            ngay_cap_nhat_gan_nhat,
            constants.XANG_RON_95_III.NGAY_CAP_NHAT_GAN_NHAT_BLOCK_ID,
        )

    @staticmethod
    def update_so_ngay_cap_nhat_gan_nhat(so_ngay_cap_nhat_gan_nhat: int):
        Board.update_so_ngay_cap_nhat_gan_nhat(
            so_ngay_cap_nhat_gan_nhat,
            constants.XANG_RON_95_III.SO_NGAY_CAP_NHAT_GAN_NHAT_BLOCK_ID,
        )

    @staticmethod
    def update_tinh_trang(tinh_trang: str):
        Board.update_tinh_trang(
            tinh_trang, constants.XANG_RON_95_III.TINH_TRANG_BLOCK_ID
        )


class XANG_E5_RON_92_II(Board):
    @staticmethod
    def update_gia_hien_tai(gia_hien_tai: float):
        Board.update_gia_hien_tai(
            gia_hien_tai, constants.XANG_E5_RON_92_II.GIA_HIEN_TAI_BLOCK_ID
        )

    @staticmethod
    def update_ngay_cap_nhat_gan_nhat(ngay_cap_nhat_gan_nhat: str):
        Board.update_ngay_cap_nhat_gan_nhat(
            ngay_cap_nhat_gan_nhat,
            constants.XANG_E5_RON_92_II.NGAY_CAP_NHAT_GAN_NHAT_BLOCK_ID,
        )

    @staticmethod
    def update_so_ngay_cap_nhat_gan_nhat(so_ngay_cap_nhat_gan_nhat: int):
        Board.update_so_ngay_cap_nhat_gan_nhat(
            so_ngay_cap_nhat_gan_nhat,
            constants.XANG_E5_RON_92_II.SO_NGAY_CAP_NHAT_GAN_NHAT_BLOCK_ID,
        )

    @staticmethod
    def update_tinh_trang(tinh_trang: str):
        Board.update_tinh_trang(
            tinh_trang, constants.XANG_E5_RON_92_II.TINH_TRANG_BLOCK_ID
        )


def get_user_ids():
    url = f"https://api.notion.com/v1/blocks/{constants.USER_CONTAINER_BLOCK_ID}/children?page_size=100"
    response = requests.get(url, headers=headers)
    data = response.json()
    user_ids = [
        block["paragraph"]["rich_text"][0]["mention"]["user"]["id"]
        for block in data["results"]
    ]
    return user_ids


def clear_mentions():
    url = f"https://api.notion.com/v1/blocks/{constants.MENTIONS_CONTAINER_BLOCK_ID}/children?page_size=100"
    response = requests.get(url, headers=headers)
    data = response.json()
    mention_block_ids = [block["id"] for block in data["results"]]
    for mention_block_id in mention_block_ids:
        url = f"https://api.notion.com/v1/blocks/{mention_block_id}"
        response = requests.delete(url, headers=headers)
        print(response)


def send_mentions(user_ids):
    data = {
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "mention",
                            "mention": {
                                "type": "user",
                                "user": {
                                    "object": "user",
                                    "id": user_id,
                                },
                            },
                        }
                    ]
                },
            }
            for user_id in user_ids
        ]
    }
    url = f"https://api.notion.com/v1/blocks/{constants.MENTIONS_CONTAINER_BLOCK_ID}/children"
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    print(response)
    return response


def send_notification():
    # Lấy các user id
    user_ids = get_user_ids()
    # Xoá các child
    clear_mentions()
    # Thêm lại các child
    send_mentions(user_ids)


if __name__ == "__main__":
    # print(send_notification())
    # print(XANG_RON_95_III.update_gia_hien_tai(199.9))
    # print(XANG_RON_95_III.update_ngay_cap_nhat_gan_nhat("05/08/2024"))
    # print(XANG_RON_95_III.update_so_ngay_cap_nhat_gan_nhat(199))
    # print(XANG_RON_95_III.update_tinh_trang("Giảm"))

    # print(XANG_E5_RON_92_II.update_gia_hien_tai(100.1))
    # print(XANG_E5_RON_92_II.update_ngay_cap_nhat_gan_nhat("08/05/2023"))
    # print(XANG_E5_RON_92_II.update_so_ngay_cap_nhat_gan_nhat(10))
    # print(XANG_E5_RON_92_II.update_tinh_trang("Tăng"))

    # send_notification()
    # response = log("06/08/2024", "Báo lỗi giả")
    # print(response.content)
    pass