export default {
  chartData: {
    labels: [],
    datasets: [{data: []}]
  },
  chartOptions: {
    maintainAspectRatio: true,
    aspectRatio: 1,
    layout: {
      padding: 5
    },
    plugins: {
      legend: {
        display: false,
        labels: {
          font: {
            size: 18
          }
        }
      },
      tooltip: {
        titleFont: {
          size: 20
        },
        titleAlign: 'center',
        boxPadding: 10
      },
      title: {
        font: {
          size: 30
        },
        display: false,
        text: ''
      }
    },
  }
}
