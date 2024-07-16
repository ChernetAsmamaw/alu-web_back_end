// building class
// error if class that extends it doesn't have evacuationWarningMessage method

export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building
      && typeof this.evacuationWarningMessage === undefined) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  set sqft(newSqft) {
    this._sqft = newSqft;
  }

  get sqft() {
    return this._sqft;
  }
}
