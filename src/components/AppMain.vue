<script>
import axios from "axios";
export default {
  name: "AppMain",
  data() {
    return {
      buy: true,
      coin: "USDT",
      forex: "RUB",
      spot: false,
      banks: [
        {
          id: 1,
          name: "Тинькофф",
          active: false,
        },
        {
          id: 2,
          name: "Сбербанк",
          active: false,
        },
        {
          id: 3,
          name: "Почта банк",
          active: false,
        },
        {
          id: 4,
          name: "Райф",
          active: false,
        },
        {
          id: 5,
          name: "Т-Банк",
          active: false,
        },
        {
          id: 6,
          name: "Тильда",
          active: false,
        },
      ],
      bank: "",
      bank_active: false,
      banks_active: [],
      mexc: [
        {
          id: 1,
          title: "Вадим",
          available: 50000,
          limit_from: 100,
          limit_to: 10000,
          price: 87.96,
          banks: ["Volet"],
        },
        {
          id: 1,
          title: "Вадим",
          available: 50000,
          limit_from: 100,
          limit_to: 10000,
          price: 87.96,
          banks: ["Volet"],
        },
        {
          id: 1,
          title: "Вадим",
          available: 50000,
          limit_from: 100,
          limit_to: 10000,
          price: 87.96,
          banks: ["Volet"],
        },
        {
          id: 1,
          title: "Вадим",
          available: 50000,
          limit_from: 100,
          limit_to: 10000,
          price: 87.96,
          banks: ["Volet"],
        },
        {
          id: 1,
          title: "Вадим",
          available: 50000,
          limit_from: 100,
          limit_to: 10000,
          price: 87.96,
          banks: ["Volet"],
        },
        {
          id: 1,
          title: "Вадим",
          available: 50000,
          limit_from: 100,
          limit_to: 10000,
          price: 87.96,
          banks: ["Volet", "Сбер"],
        },
        {
          id: 1,
          title: "Вадим",
          available: 50000,
          limit_from: 100,
          limit_to: 10000,
          price: 87.96,
          banks: ["Volet", "Тинькофф"],
        },
      ],
      bybit: [],
      kucoin: [],
      title: "",
      available: 0,
      limit_from: 0,
      limit_to: 0,
      price: 0,
      banks_card: [],
      main_active: false,
    };
  },
  methods: {
    async log() {
      this.$emit("updateLogin", false);
    },
    buysell(f) {
      this.buy = f;
    },
    spotp2p(f) {
      this.spot = f;
    },

    bankClick(id) {
      for (let i = 0; i < this.banks.length; i++) {
        let bank = this.banks[i];
        if (bank.id == id) {
          if (bank.active) {
            bank.active = false;
            this.banks_active = this.banks_active.filter(
              (item) => item != bank.name
            );
          } else {
            bank.active = true;
            this.banks_active.push(bank.name);
          }
        }
        this.banks[i] = bank;
      }
    },

    activeMain(card) {
      this.main_active = true;
      this.title = card.title;
      this.banks_card = card.banks;
      this.available = card.available;
      this.limit_to = card.limit_to;
      this.limit_from = card.limit_from;
      this.price = card.price;
    },

    printBank(id) {
      let bank = this.banks.find((bank) => bank.id == id);
      return bank ? bank.name : null; // Возвращает имя банка, если найден, иначе null
    },

    async load_info() {
      try {
        if (this.spot) {
          let response = await axios.post(`/spot`);
          console.log(response);
        } else {
          if (this.price) {
            this.price = JSON.stringify(this.price);
          }
          if (this.buy) {
            this.buy = "1";
          } else {
            this.buy = "0";
          }
          let banks = [];
          if (this.banks_active) {
            this.banks_active.forEach((item) => {
              let bank = this.banks.find((bank) => bank.name == item);
              banks.push(bank.id);
            });
          }
          console.log(banks);
          let response = await axios.post(`/admin`, {
            params: {
              tokenId: this.coin || "USDT",
              currencyId: this.forex || "RUB",
              amount: this.price,
              paymant: banks,
              side: this.buy,
            },
          });
          this.banks = response.data.only_code_bank_bybit;
          this.bybit = response.data.price_byb;
          this.kucoin = response.data.price_kuc;
          console.log(response);
        }
      } catch (err) {
        console.log(err);
      }
    },
  },
  mounted() {
    this.load_info();
  },
};
</script>
<template>
  <div class="wrapper">
    <div class="filter">
      <div class="buysell">
        <button @click="buysell(true)" class="btn" :class="{ buy: this.buy }">
          Покупка
        </button>
        <button
          @click="buysell(false)"
          class="btn"
          :class="{ sell: !this.buy }"
        >
          Продажа
        </button>
      </div>
      <select class="coin" v-model="coin" id="">
        <option value="BTC">BTC</option>
        <option value="ETH">ETH</option>
        <option value="USDT">USDT</option>
        <option value="NOT">NOT</option>
      </select>
      <div class="group">
        <input type="number" class="sum" placeholder="Введите сумму" />
        <select v-model="forex" id="">
          <option value="RUB">RUB</option>
          <option value="USD">USD</option>
          <option value="EUR">EUR</option>
        </select>
      </div>
      <div class="group-bank">
        <input
          type="text"
          @click="bank_active = !bank_active"
          v-model="banks_active"
          placeholder="Все способы оплаты"
        />
        <div class="banks" v-if="bank_active">
          <div
            class="bank"
            v-for="bank in banks"
            :key="bank.id"
            @click="bankClick(bank.id)"
            :class="{ bank_active: bank.active }"
          >
            {{ bank.name }}
          </div>
        </div>
      </div>
      <div class="spotp2p">
        <button @click="spotp2p(true)" class="btn" :class="{ spot: this.spot }">
          Спот
        </button>
        <button
          @click="spotp2p(false)"
          class="btn"
          :class="{ p2p: !this.spot }"
        >
          p2p
        </button>
      </div>
      <button class="btn apply" @click="load_info()">Применить</button>
    </div>
    <div class="market">
      <div class="marcol">
        <div class="title">Mexc</div>
      </div>
      <div class="marcol">
        <div class="title">BitPapa</div>
      </div>
      <div class="marcol">
        <div class="title">BingX</div>
      </div>
      <div class="marcol">
        <div class="title">BitGet</div>
      </div>
      <div class="marcol">
        <div class="title">ByBit</div>
      </div>
      <div class="marcol">
        <div class="title">Abcex</div>
      </div>
      <div class="marcol">
        <div class="title">KuCoin</div>
      </div>
    </div>
    <div class="offers">
      <div class="cards">
        <div
          class="card"
          @click="activeMain(card)"
          v-for="card in mexc"
          :key="card.id"
        >
          <div class="title">{{ card.title }}</div>
          <div class="available">
            <span>Доступно:</span> {{ card.available }}
          </div>
          <div class="limits">
            <span>от</span> {{ card.limit_from }} <span>до</span>
            {{ card.limit_to }} <span>RUB</span>
          </div>
          <div class="price">{{ card.price }} <span>RUB</span></div>
          <div class="offer_banks">
            <div class="offer_bank" v-for="bank in card.banks" :key="bank">
              {{ bank }}
            </div>
          </div>
        </div>
      </div>
      <div class="cards">
        <div
          class="card"
          @click="activeMain(card)"
          v-for="card in mexc"
          :key="card.id"
        >
          <div class="title">{{ card.title }}</div>
          <div class="available">
            <span>Доступно:</span> {{ card.available }}
          </div>
          <div class="limits">
            <span>от</span> {{ card.limit_from }} <span>до</span>
            {{ card.limit_to }} <span>RUB</span>
          </div>
          <div class="price">{{ card.price }} <span>RUB</span></div>
          <div class="offer_banks">
            <div class="offer_bank" v-for="bank in card.payments" :key="bank">
              {{ printBank(bank) }}
            </div>
          </div>
        </div>
      </div>
      <div class="cards">
        <div
          class="card"
          @click="activeMain(card)"
          v-for="card in mexc"
          :key="card.id"
        >
          <div class="title">{{ card.title }}</div>
          <div class="available">
            <span>Доступно:</span> {{ card.available }}
          </div>
          <div class="limits">
            <span>от</span> {{ card.limit_from }} <span>до</span>
            {{ card.limit_to }} <span>RUB</span>
          </div>
          <div class="price">{{ card.price }} <span>RUB</span></div>
          <div class="offer_banks">
            <div class="offer_bank" v-for="bank in card.banks" :key="bank">
              {{ bank }}
            </div>
          </div>
        </div>
      </div>
      <div class="cards">
        <div
          class="card"
          @click="activeMain(card)"
          v-for="card in mexc"
          :key="card.id"
        >
          <div class="title">{{ card.title }}</div>
          <div class="available">
            <span>Доступно:</span> {{ card.available }}
          </div>
          <div class="limits">
            <span>от</span> {{ card.limit_from }} <span>до</span>
            {{ card.limit_to }} <span>RUB</span>
          </div>
          <div class="price">{{ card.price }} <span>RUB</span></div>
          <div class="offer_banks">
            <div class="offer_bank" v-for="bank in card.banks" :key="bank">
              {{ bank }}
            </div>
          </div>
        </div>
      </div>
      <div class="cards">
        <div
          class="card"
          @click="activeMain(card)"
          v-for="card in bybit"
          :key="card.id"
        >
          <div class="title">{{ card.nickName }}</div>
          <div class="available">
            <span>Доступно:</span> {{ card.lastQuantity }}
          </div>
          <div class="limits">
            <span>от</span> {{ card.minAmount }} <span>до</span>
            {{ card.maxAmount }} <span>RUB</span>
          </div>
          <div class="price">{{ card.price }} <span>RUB</span></div>
          <div class="offer_banks">
            <div class="offer_bank" v-for="bank in card.payments" :key="bank">
              {{ printBank(bank) }}
            </div>
          </div>
        </div>
      </div>
      <div class="cards">
        <div
          class="card"
          @click="activeMain(card)"
          v-for="card in mexc"
          :key="card.id"
        >
          <div class="title">{{ card.title }}</div>
          <div class="available">
            <span>Доступно:</span> {{ card.available }}
          </div>
          <div class="limits">
            <span>от</span> {{ card.limit_from }} <span>до</span>
            {{ card.limit_to }} <span>RUB</span>
          </div>
          <div class="price">{{ card.price }} <span>RUB</span></div>
          <div class="offer_banks">
            <div class="offer_bank" v-for="bank in card.banks" :key="bank">
              {{ bank }}
            </div>
          </div>
        </div>
      </div>
      <div class="cards">
        <div
          class="card"
          @click="activeMain(card)"
          v-for="card in kucoin"
          :key="card.id"
        >
          <div class="title">{{ card.nickName }}</div>
          <div class="available">
            <span>Доступно:</span> {{ card.currencyBalanceQuantity }}
          </div>
          <div class="limits">
            <span>от</span> {{ card.limitMinQuote }} <span>до</span>
            {{ card.limitMaxQuote }} <span>RUB</span>
          </div>
          <div class="price">{{ card.floatPrice }} <span>RUB</span></div>
          <div class="offer_banks">
            <div class="offer_bank" v-for="bank in card.adPayTypes" :key="bank">
              {{ bank.payTypeCode }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="main_card" v-if="main_active">
      <div class="btns">
        <img
          @click="this.main_active = false"
          class="close"
          src="../assets/close.png"
          alt=""
        />
      </div>
      <div class="main_title">{{ title }}</div>
      <div class="main_available"><span>Доступно:</span> {{ available }}</div>
      <div class="main_limits">
        <span>от</span> {{ limit_from }} <span>до</span> {{ limit_to }}
        <span>RUB</span>
      </div>
      <div class="main_price">{{ price }} <span>RUB</span></div>
      <div class="main_offer_banks">
        <div class="main_offer_bank" v-for="bank in banks_card" :key="bank">
          {{ bank }}
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.wrapper {
  padding: 50px;
  display: flex;
  flex-direction: column;
  gap: 30px;
  position: relative;
}

.main_card {
  position: absolute;
  background-color: #f5f5f8;
  border-radius: 10px;
  box-shadow: 0 0 15px 0 #00000037;
  top: 50%; /* Центрирование по вертикали */
  left: 50%; /* Центрирование по горизонтали */
  transform: translate(-50%, -50%);
  padding: 20px;
  min-width: 250px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 3;
}

.main_title,
.main_price {
  font-weight: 600;
  font-size: 20px;
}

.main_title span,
.main_price span,
.main_limits span,
.main_available span {
  font-size: 14px;
  opacity: 50%;
}

.btns {
  width: 100%;
  display: flex;
  justify-content: end;
}
.close {
  width: 20px;
  height: 20px;
  cursor: pointer;
  transition: all 400ms ease;
}

.close:hover {
  transform: scale(1.02);
}

.market,
.offers {
  background-color: #fff;
  padding: 20px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 5px;
  box-shadow: 0 0 15px 0 #00000037;
}

.market {
  position: sticky;
  top: 0;
  z-index: 2;
}

.marcol {
  flex: 15%;
}

.title {
  font-weight: 600;
}

.filter {
  display: flex;
  align-items: center;
  gap: 25px;
  border-radius: 12px;
}
.buysell {
  display: flex;
  align-items: center;
  gap: 3px;
  padding: 3px;
  background-color: #fff;
  border-radius: 10px;
}

.btn {
  padding: 10px 15px;
  background-color: #f0f0f5;
  font-weight: 500;
  transition: all 500ms ease;
  border-radius: 10px;
}

.apply {
  background-color: #45ed0b;
  color: #fff;
}

.sell {
  color: #fff;
  background-color: #cf0032;
}

.buy {
  color: #fff;
  background-color: #45ed0b;
}

.coin {
  background-color: #fff;
  border-radius: 10px;
  padding: 10px 15px;
}

.group input {
  padding: 10px 15px;
  background-color: #fff;
  border-radius: 10px 0 0 10px;
}

.group-bank {
  position: relative;
}

.banks {
  width: 100%;
  background-color: #f0f0f5;
  border-radius: 10px;
  padding: 10px 12px;
  z-index: 3;
  position: absolute;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 5px;
  max-height: 300px;
  overflow-x: hidden;
  overflow-y: scroll;
}

.bank {
  flex: 45%;
  cursor: pointer;
  user-select: none; /* Для Webkit браузеров (Chrome, Safari) */
  -webkit-user-select: none; /* Для Firefox */
  -moz-user-select: none; /* Для IE */
  -ms-user-select: none; /* Для Edge */
  padding: 3px 5px;
  border-radius: 7px;
  font-weight: 500;
}

.bank_active {
  background-color: #f0c808;
}

.group-bank input {
  padding: 10px 15px;
  background-color: #fff;
  border-radius: 10px;
}

.group select {
  padding: 9px 7px;
  background-color: #fff;
  border-radius: 0 10px 10px 0;
}

.spotp2p {
  background-color: #fff;
  padding: 3px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  gap: 3px;
}

.spot {
  color: #fff;
  background-color: #1a1423;
}

.p2p {
  color: #fff;
  background-color: #086788;
}

.cards {
  border-right: 1px solid #f0c808;
  padding-right: 3px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.cards:last-child,
.card:first-child {
  border: none;
}

.card {
  display: flex;
  flex-direction: column;
  gap: 5px;
  border-top: 1px solid #f0c808;
  padding: 3px 0;
}

.card:hover {
  transform: scale(1.06);
}

.card span {
  font-size: 12px;
  font-weight: 500;
  opacity: 50%;
}

.available,
.limits {
  font-weight: 600;
  font-size: 14px;
  opacity: 70%;
}

.price {
  font-weight: 600;
  text-align: center;
  font-size: 20px;
}

.offer_banks,
.main_offer_banks {
  display: flex;
  flex-wrap: wrap;
  gap: 3px;
}

.offer_bank,
.main_offer_bank {
  width: fit-content;
  background-color: #f0c808;
  color: black;
  font-weight: 600;
  font-size: 12px;
  padding: 1px 3px;
  border-radius: 2px;
}

@media (max-width: 1150px) {
  .filter {
    gap: 10px;
    flex-wrap: wrap;
  }
}

@media (max-width: 865px) {
  .wrapper {
    padding: 10px;
    gap: 15px;
  }
}

@media (max-width: 680px) {
  .available,
  .limits,
  .offer_banks {
    display: none;
  }
}

@media (max-width: 500px) {
  .market {
    padding: 8px;
  }

  .card .title {
    display: none;
  }

  .market .title {
    font-size: 10px;
  }

  .offers {
    padding: 5px;
  }

  .price {
    font-size: 16px;
  }

  .filter {
    gap: 5px;
    justify-content: center;
  }

  button,
  input,
  select {
    font-size: 12px;
    padding: 3px 5px;
  }
}

@media (max-width: 375px) {
  .market,
  .offers {
    gap: 0;
  }

  .price {
    font-size: 13px;
  }
}
</style>
