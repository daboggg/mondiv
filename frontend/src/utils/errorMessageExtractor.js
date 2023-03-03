export default function (errors) {
  const res = []
  Object.keys(errors).forEach(key => errors[key].forEach(it => res.push(it)))
  return res.join('<br>')
}