// Function named loadBalancer accepts two arguments both are promises.

export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
