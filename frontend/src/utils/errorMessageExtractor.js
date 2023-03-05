export default function (errors) {
  const res = []
  // Object.keys(errors).forEach(key => errors[key].forEach(it => res.push(it)))
  Object.keys(errors).forEach(key => {
    if (Array.isArray(errors[key])) {
      errors[key].forEach(it => res.push(it));
    } else {
      res.push(errors[key])
    }
  })
  return res.join('<br>')
}