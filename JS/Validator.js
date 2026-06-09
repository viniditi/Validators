export default class Validator {
  CNPJAlfanumerico(CNPJ) {
    if (!CNPJ) {
      throw new TypeError("CNPJ não foi informado ou está vazio.");
    }

    if (this.todosDigitosIguais(CNPJ)) {
      throw new Error("CNPJ com todos os caracteres são iguais.");
    }

    const CNPJSemMascara = this.RemoveMaskCNPJ(CNPJ);

    if (CNPJSemMascara.length !== 14) {
      throw new Error("CNPJ com o valor menor ou maior que 14 digitos.");
    }

    const CnpjParcializado = CNPJSemMascara.slice(0, -2);
    const digitosCalculados = [];

    for (let i = 0; i < 2; i++) {
      CnpjParcializado.push(String(this.TotalCNPJHelper(CnpjParcializado)));
    }

    const resultado = CnpjParcializado.join("");

    if (resultado === CNPJSemMascara.join("")) {
      return true;
    }

    return false;
  }

  TotalCNPJHelper(CNPJSliced) {
    let peso;

    if (CNPJSliced.length === 12) {
      peso = "543298765432";
    } else {
      peso = "6543298765432";
    }

    const total = CNPJSliced.reduce((acc, curr, index) => {
      let count = Number(curr.charCodeAt(0)) - 48;
      count = count * peso[index];
      return acc + count;
    }, 0);

    console.log(tota);

    let resultado = total % 11;

    if (resultado === 0 || resultado === 1) {
      resultado = 0;
    } else {
      resultado = 11 - resultado;
    }

    return resultado;
  }

  RemoveMaskCNPJ(CNPJMascarado) {
    return CNPJMascarado.split("").filter(
      (letter) => ![".", "/", "-"].includes(letter),
    );
  }

  todosDigitosIguais(str) {
    return str.split("").every((digito) => digito === str[0]);
  }
}
