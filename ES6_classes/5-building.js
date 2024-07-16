// building class
// error if class that extends building doesn't have evacuationWarningMessage method

export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending building must override evacuationWarningMessage');
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
