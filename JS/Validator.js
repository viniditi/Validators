export default class Validator {
  ValidateCNPJ(CNPJ) {
    if (!CNPJ) {
      throw new TypeError("CNPJ is empty or Null.");
    }

    if (this.EqualDigits(CNPJ)) {
      throw new Error("CNPJ has all equals characters.");
    }

    const CNPJWithoutMask = this.RemoveMaskCNPJ(CNPJ);

    if (CNPJWithoutMask.length !== 14) {
      throw new Error("CNPJ has more or less than 14 characters.");
    }

    const slicedCNPJ = CNPJWithoutMask.slice(0, -2);

    for (let i = 0; i < 2; i++) {
      slicedCNPJ.push(String(this.TotalCNPJ(slicedCNPJ)));
    }

    const result = slicedCNPJ.join("");

    if (result === CNPJWithoutMask.join("")) {
      return true;
    }

    return false;
  }

  TotalCNPJ(CNPJSliced) {
    let weight;

    if (CNPJSliced.length === 12) {
      weight = "543298765432";
    } else {
      weight = "6543298765432";
    }

    const total = CNPJSliced.reduce((acc, curr, index) => {
      let count = Number(curr.charCodeAt(0)) - 48;
      count = count * weight[index];
      return acc + count;
    }, 0);

    let result = total % 11;

    if (result === 0 || result === 1) {
      result = 0;
    } else {
      result = 11 - result;
    }

    return result;
  }

  RemoveMaskCNPJ(maskedCNPJ) {
    return maskedCNPJ
      .split("")
      .filter((letter) => ![".", "/", "-"].includes(letter));
  }

  EqualDigits(cnpj) {
    return cnpj.split("").every((digit) => digit === cnpj[0]);
  }
}
