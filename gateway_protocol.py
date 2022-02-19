from gateway import GatewayCon

LIB_NAME = "tmtc-dispy"
x = 1 << 10

class Gateway(GatewayCon):
    async def handle_message(self, msg):
        print(msg)
        if msg.op == 10:
            print("got HELLO, sending identify")
            self._pulse = msg.data.heartbeat_interval / 1000
            identity = {
                "op": 2,
                "d": {
                    "token": self._token,
                    "intents": x,
                    "properties": {
                        "$os": "windows",
                        "$browser": LIB_NAME,
                        "$device": LIB_NAME,
                    }
                },
            }
            await self.send(identity)
            print("done identify")
        else:
            raise Exception(f"unknow op in messafe {msg.op}")

if __name__ == "__main__":
    with open(".token") as token_file:
        token = token_file.read()[:-1]
        g = Gateway(token)
        g.run()